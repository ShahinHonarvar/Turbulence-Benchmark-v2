def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def leading_digit_removed(n):
        return int(str(n)[1:])
    left_truncatable_primes = []
    for num in range(2, x):
        for leading_digit in '123456789':
            if not is_prime(int(leading_digit + str(num))):
                break
            num = leading_digit_removed(num)
        else:
            left_truncatable_primes.append(int(str(num)))
    return sorted(left_truncatable_primes)