def all_left_truncatable_prime(n):
    x = n[70]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def trunc_prime(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(len(s))))
    return sorted([i for i in range(2, x) if '0' not in str(i) and trunc_prime(i)], reverse=True)