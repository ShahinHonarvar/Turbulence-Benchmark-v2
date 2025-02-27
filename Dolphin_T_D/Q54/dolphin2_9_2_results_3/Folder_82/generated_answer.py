def all_right_truncatable_prime(tuple_of_integers):

    def _is_right_truncatable_prime(n):
        if str(n)[-1] in '245689':
            return False
        while n > 1 and _is_prime(n):
            n /= 10
        return n == 1

    def _is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = tuple_of_integers[69]
    return sorted([n for n in range(2, x) if _is_right_truncatable_prime(n)], reverse=True)