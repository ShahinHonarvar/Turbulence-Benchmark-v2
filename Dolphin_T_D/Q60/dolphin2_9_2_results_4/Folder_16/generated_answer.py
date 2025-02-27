def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[792]
    result = []
    for i in range(2, x + 1):
        if '0' not in str(i):
            s = str(i)
            if is_prime(int(s)):
                while len(s) > 1:
                    if not is_prime(int(s[1:-1])):
                        break
                    s = s[1:-1]
                    if is_prime(int(s)):
                        result.append(int(s))
    return sorted(set(result))