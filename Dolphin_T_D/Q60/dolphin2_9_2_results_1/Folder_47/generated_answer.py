def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[49]
    result = []
    for n in range(2, x + 1):
        if '0' not in str(n):
            n_str = str(n)
            while len(n_str) > 1:
                if not is_prime(int(n_str)):
                    break
                n_str = n_str[1:-1]
            else:
                result.append(n)
    result.sort()
    return result