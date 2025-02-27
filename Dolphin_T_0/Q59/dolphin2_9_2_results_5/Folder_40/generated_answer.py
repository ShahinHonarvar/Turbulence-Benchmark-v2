def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True
    x = num_tuple[10]
    trunc_list = []
    for n in range(2, x):
        str_n = str(n)
        if '0' in str_n:
            continue
        if str_n[0] != '0':
            trunc = str_n[1:]
            while trunc:
                if not is_prime(int(trunc)):
                    break
                trunc = trunc[1:]
            else:
                trunc_list.append(n)
    return sorted(trunc_list, reverse=True)