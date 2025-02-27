def all_left_truncatable_prime(x):

    def _is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def _is_truncatable(n):
        if n < 10:
            return True
        new_n = n // 10
        return _is_prime(new_n) and _is_truncatable(new_n)
    prime_numbers = []
    num = 2
    while num < x:
        if _is_prime(num) and _is_truncatable(num):
            prime_numbers.append(num)
        num += 1
    return sorted(prime_numbers)