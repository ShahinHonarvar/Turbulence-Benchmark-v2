def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[74]
    res = []
    for i in range(2, x):
        number = str(i)
        if all(('0' not in str(i // 10 ** j) and is_prime(i // 10 ** j) for j in range(len(number)))):
            res.append(i)
    return sorted(res)