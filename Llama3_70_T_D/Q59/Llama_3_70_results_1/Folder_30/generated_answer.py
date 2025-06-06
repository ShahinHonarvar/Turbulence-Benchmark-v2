def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[37]
    left_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if is_prime(num):
            is_left_truncatable_prime = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    is_left_truncatable_prime = False
                    break
            if is_left_truncatable_prime:
                left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes