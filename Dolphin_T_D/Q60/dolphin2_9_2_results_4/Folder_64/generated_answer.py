def all_left_right_truncatable_prime(num_range):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_range[4]
    truncatable_prime_nums = []
    for num in range(x + 1):
        if is_prime(num):
            trunc = str(num)
            while len(trunc) > 1:
                if len(trunc) == 2:
                    truncatable_prime_nums.append(int(trunc))
                trunc = trunc[1:-1]
                if not is_prime(int(trunc)):
                    break
    return truncatable_prime_nums