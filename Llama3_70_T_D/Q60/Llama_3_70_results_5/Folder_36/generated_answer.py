def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n ** 0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True
    x = numbers[992]
    left_right_truncatable_primes = []
    for n in range(10, x + 1):
        if '0' not in str(n):
            digits = list(str(n))
            is_left_right_truncatable = True
            for _ in range(len(digits) - 1):
                digits = digits[1:-1]
                if len(digits) > 0 and (not is_prime(int(''.join(digits)))):
                    is_left_right_truncatable = False
                    break
            if is_left_right_truncatable and is_prime(n):
                left_right_truncatable_primes.append(n)
    return left_right_truncatable_primes.sort() or left_right_truncatable_primes