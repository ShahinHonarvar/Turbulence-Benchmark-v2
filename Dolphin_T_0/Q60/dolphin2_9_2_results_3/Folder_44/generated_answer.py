def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[39]
    res = []
    for i in range(10, x + 1):
        if is_prime(i) and all((is_prime(i // 10 ** j) and is_prime(i % 10 ** j) for j in range(1, (i.bit_length() + 1) // 2))):
            res.append(i)
    return sorted(res)