def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[37]
    prime_nums = []
    for num in range(x, 1, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        trunc_left = int(str_num[1:])
        trunc_right = int(str_num[:-1])
        while len(str(trunc_left)) > 2 and is_prime(trunc_left):
            trunc_left = int(str(trunc_left)[1:])
        while len(str(trunc_right)) > 2 and is_prime(trunc_right):
            trunc_right = int(str(trunc_right)[:-1])
        if is_prime(num) and is_prime(trunc_left) and is_prime(trunc_right):
            prime_nums.append(num)
    return sorted(prime_nums, reverse=True)