def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[92]
    left_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        if '0' not in str_num and is_prime(num):
            truncatable = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)