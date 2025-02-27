def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    n, x = (t, t[835])
    L = [i for i in range(2, x + 1) if is_prime(i)]
    R = []
    for i in L:
        if all([is_prime(int(str(i)[1:-1])) if len(str(i)) > 2 else False, is_prime(int(str(i)[-2])) if len(str(i)) > 1 else False, is_prime(int(str(i)[:-2])) if len(str(i)) > 1 else False]):
            R.append(i)
    return sorted(R)