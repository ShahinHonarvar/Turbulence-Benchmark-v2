def all_left_truncatable_prime(tuples):
    x = tuples[91]

    def is_prime(n):
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

    def is_left_truncatable(n):
        str_n = str(n)
        return all((is_prime(int(str_n[i:])) for i in range(len(str_n))))
    return sorted([n for n in range(2, x) if is_left_truncatable(n)])