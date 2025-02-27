def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[30]
    result = []
    for i in range(2, x + 1):
        if is_prime(i):
            str_i = str(i)
            while str_i and is_prime(int(str_i)):
                if str_i[0] == str_i[-1]:
                    result.append(int(str_i))
                str_i = str_i[1:-1]
    return sorted(result)