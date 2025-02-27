def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n in (0, 1):
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True
    x = num_tuple[767]
    left_truncatable_prime_nums = []
    for num in range(x, 0, -1):
        if is_prime(num):
            str_num = str(num)
            left_truncatable = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    left_truncatable = False
                    break
            if left_truncatable:
                left_truncatable_prime_nums.append(num)
    return sorted(left_truncatable_prime_nums, reverse=True)