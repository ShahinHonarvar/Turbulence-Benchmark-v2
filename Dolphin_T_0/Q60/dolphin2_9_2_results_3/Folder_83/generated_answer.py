def all_left_right_truncatable_prime(args):

    def is_prime_n(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = args[24]
    left_right_truncatables = []
    for n in range(2, x + 1):
        str_n = str(n)
        if '0' in str_n or not is_prime_n(n):
            continue
        while len(str_n) > 1:
            if not is_prime_n(int(str_n[1:-1])):
                break
            str_n = str_n[1:-1]
            if len(str_n) == 0:
                left_right_truncatables.append(n)
                break
    return sorted(left_right_truncatables)