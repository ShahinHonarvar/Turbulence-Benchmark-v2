def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[41]
    ltp_list = []
    for i in range(x - 1, 0, -1):
        str_i = str(i)
        if str_i.count('0'):
            continue
        if is_prime(int(str_i)):
            for j in range(len(str_i) - 1):
                if not is_prime(int(str_i[j + 1:])):
                    break
            else:
                ltp_list.append(i)
    ltp_list.sort(reverse=True)
    return ltp_list