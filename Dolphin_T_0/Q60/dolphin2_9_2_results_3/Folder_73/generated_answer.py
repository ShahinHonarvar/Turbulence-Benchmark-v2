def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_right_truncatable = []
    for i in range(1, x + 1):
        if '0' in str(i) or not is_prime(i):
            continue
        while len(str(i)) > 1:
            i = int(i / 10)
            if not is_prime(i):
                break
        else:
            left_right_truncatable.append(i)
    left_right_truncatable.sort()
    return left_right_truncatable