def all_right_truncatable_prime(t):
    x = t[70]

    def prime(n):
        return all((n % k != 0 for k in range(2, int(n ** 0.5))))
    res = []
    for i in range(2, x):
        if prime(i):
            for j in str(i)[:-1:-1]:
                if not prime(int(j)):
                    break
            else:
                res.append(i)
    return sorted(res)