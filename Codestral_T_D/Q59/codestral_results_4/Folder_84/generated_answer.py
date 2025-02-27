def all_left_truncatable_prime(numbers):
    x = numbers[630]

    def is_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_all_truncated_prime(n):
        while n:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True
    return sorted(filter(is_all_truncated_prime, range(3, x)), reverse=True)