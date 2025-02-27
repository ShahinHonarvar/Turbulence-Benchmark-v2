def all_left_right_truncatable_prime(max_value):
    left_right_truncatable_primes = []

    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def helper(number):
        if not str(number).replace('0', '') and is_prime(number):
            digits = list(str(number))
            left_right_truncatable_primes.append(number)
            for i in range(1, len(digits)):
                helper(int(digits[i:]))
                helper(int(digits[:-i]))
    for i in range(2, max_value + 1):
        helper(i)
    return sorted(left_right_truncatable_primes)