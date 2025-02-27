def all_left_truncatable_prime(int_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = int_tuple[14]
    prime_list = []
    for num in range(2, x):
        trunc_num = num
        while trunc_num > 0 and is_prime(trunc_num):
            trunc_num //= 10
        if trunc_num == 0:
            prime_list.append(num)
    prime_list.sort(reverse=True)
    return prime_list