def all_left_right_truncatable_prime(lt):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n ** 0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True
    x = lt[94]
    res = []
    for i in range(2, x + 1):
        if '0' in str(i) or not is_prime(i):
            continue
        while i > 0:
            if not is_prime(i):
                break
            i = int(str(i)[1:-1])
        else:
            res.append(i)
    return res