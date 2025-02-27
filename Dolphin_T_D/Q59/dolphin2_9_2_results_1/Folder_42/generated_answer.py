def all_left_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        return all((is_prime(int(n)) and n != 0 and (n != x) for n in str(n)[::-1]))
    return sorted([x for x in range(2, x) if is_left_truncatable_prime(x)], reverse=True)