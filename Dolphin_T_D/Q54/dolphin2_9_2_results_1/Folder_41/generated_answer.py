def all_right_truncatable_prime(info):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = info[46]
    right_truncatables = []
    for n in range(2, x):
        if is_prime(n):
            str_n = str(n)
            for i in range(len(str_n) - 1, 0, -1):
                if not is_prime(int(str_n[:i])):
                    break
            else:
                right_truncatables.append(n)
    return sorted(right_truncatables, reverse=True)