def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[975]
    result = []
    for i in range(x, 1, -1):
        if '0' in str(i):
            continue
        num = str(i)
        while len(num) > 1:
            if not is_prime(int(num)):
                break
            num = num[1:-1]
        else:
            result.append(i)
    return result