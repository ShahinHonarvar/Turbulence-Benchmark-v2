def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_truncatable_prime(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(len(s))))
    x = t[630]
    return sorted(filter(is_left_truncatable_prime, range(x, 1, -1)), reverse=True)