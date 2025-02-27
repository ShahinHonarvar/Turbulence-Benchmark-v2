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

def all_right_truncatable_prime(numbers):
    x = numbers[92]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncated_num = str(num)
            is_right_truncatable = True
            for i in range(1, len(truncated_num)):
                if not is_prime(int(truncated_num[:-i])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)