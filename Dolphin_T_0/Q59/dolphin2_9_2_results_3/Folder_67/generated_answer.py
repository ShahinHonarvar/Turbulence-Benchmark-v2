def all_left_truncatable_prime(num_tuple):

    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        for i in range(len(n) - 1, 0, -1):
            if not check_prime(int(n[i:])):
                return False
        return True
    x = num_tuple[71]
    result = []
    for n in range(x, 1, -1):
        if check_prime(n) and is_truncatable_prime(n):
            result.append(n)
    return result