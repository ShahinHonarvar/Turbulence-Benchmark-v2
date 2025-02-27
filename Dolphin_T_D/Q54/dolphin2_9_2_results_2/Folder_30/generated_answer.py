def all_right_truncatable_prime(tuple_of_positive_integers):

    def is_prime_number(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_of_positive_integers[37]
    all_right_truncatable_prime_desc = []
    for num in range(x, 0, -1):
        if is_prime_number(num):
            trunc_num = num
            while trunc_num > 10:
                trunc_num = trunc_num // 10
                if not is_prime_number(trunc_num):
                    break
            else:
                all_right_truncatable_prime_desc.append(num)
    return sorted(all_right_truncatable_prime_desc, reverse=True)