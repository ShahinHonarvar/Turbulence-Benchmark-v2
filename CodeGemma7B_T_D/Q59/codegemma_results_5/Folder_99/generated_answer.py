def all_left_truncatable_prime(tup):
    x = tup[758]

    def is_prime(n):
        return n > 1 and all((n % i for i in range(2, int(n ** 0.5) + 1)))

    def is_left_truncatable(n):
        if n % 10 == 0:
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    ans = [i for i in range(x) if is_left_truncatable(i)]
    ans.sort()
    return ans