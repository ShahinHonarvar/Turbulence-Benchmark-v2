def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            left = int(str_n[i:])
            right = int(str_n[:i + 1])
            if not is_prime(left) or not is_prime(right) or str_n.count('0') > 0:
                return False
        return True
    x = numbers[38]
    left_right_primes = [i for i in range(x, 1, -1) if is_truncable_prime(i)]
    return sorted(left_right_primes, reverse=True)