def all_left_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = int_tuple[64]
    primes = []
    for num in range(x, 0, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        while len(str_num) > 2:
            if not is_prime(int(str_num[1:-1])):
                break
            str_num = str_num[1:-1]
        else:
            primes.append(num)
    return sorted(primes, reverse=True)