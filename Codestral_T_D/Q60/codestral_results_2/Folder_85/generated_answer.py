def all_left_right_truncatable_prime(numbers):
    x = numbers[94]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        if '0' in str(n):
            return False
        digits = [int(digit) for digit in str(n)]
        for i in range(len(digits) - 1):
            left_truncated = int(''.join(map(str, digits[i + 1:])))
            right_truncated = int(''.join(map(str, digits[:-i - 1])))
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)