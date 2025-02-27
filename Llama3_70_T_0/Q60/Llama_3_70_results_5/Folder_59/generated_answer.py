def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[84]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            str_num = str(num)
            left_truncatable = True
            right_truncatable = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                    left_truncatable = False
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)