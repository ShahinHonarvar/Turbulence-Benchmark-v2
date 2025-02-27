def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

    def is_left_truncatable(n):
        if n == 1:
            return False
        s = str(n)
        if s.count('0') > 0:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = t[429]
    prime_list = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_list = [i for i in prime_list if is_left_truncatable(i)]
    return sorted(left_truncatable_list, reverse=True)