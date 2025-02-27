def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_right_truncatable_primes = []
    for num in range(x, 1, -1):
        num_str = str(num)
        if not any((digit == '0' for digit in num_str)):
            while len(num_str) > 1:
                num_str = num_str[1:-1]
                if not is_prime(int(num_str)):
                    break
            else:
                left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort()
    return left_right_truncatable_primes