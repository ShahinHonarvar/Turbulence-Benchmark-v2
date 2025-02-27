def all_right_truncatable_prime(t):

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[370]
    s = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            for _ in range(len(str(i)) - 1):
                if not is_prime(int(str(i)[:-1])):
                    break
            else:
                s.append(i)
    return s