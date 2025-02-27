def all_left_truncatable_prime(t):

    def is_prime(n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def is_left_truncatable_prime(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(len(s))))
    x = t[36]
    return sorted([i for i in range(x, 1, -1) if is_prime(i) and is_left_truncatable_prime(i)], reverse=True)