def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    x = num_tuple[760]
    res = [i for i in range(x - 1, 1, -1) if i % 5 != 0 and i % 2 != 0 and is_prime(i)]
    for i in range(len(res)):
        if not is_prime(int(str(res[i] // 10))):
            res.remove(res[i])
    return res