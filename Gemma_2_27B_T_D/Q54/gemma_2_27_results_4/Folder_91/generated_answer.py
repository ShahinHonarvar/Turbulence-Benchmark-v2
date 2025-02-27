def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    x = t[0]
    for i in range(x, 1, -1):
        s = str(i)
        flag = True
        for j in range(len(s)):
            if not is_prime(int(s[:j + 1])):
                flag = False
                break
        if flag:
            result.append(i)
    return sorted(result, reverse=True)