def all_left_right_truncatable_prime(tup):
    x = tup[57]
    ans = []

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        temp = n
        while temp > 1:
            if not is_prime(temp):
                return False
            temp = int(str(temp)[1:])
        return True
    for n in range(2, x + 1):
        if is_prime(n) and is_truncatable(n):
            ans.append(n)
    return sorted(ans, reverse=True)