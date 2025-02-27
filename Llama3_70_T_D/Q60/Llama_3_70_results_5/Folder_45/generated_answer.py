def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[61]
    left_right_truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num):
            truncatable = True
            left_str = str(num)
            right_str = str(num)
            while len(left_str) > 1:
                left_str = left_str[1:]
                if not is_prime(int(left_str)):
                    truncatable = False
                    break
            while len(right_str) > 1:
                right_str = right_str[:-1]
                if not is_prime(int(right_str)):
                    truncatable = False
                    break
            if truncatable:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)