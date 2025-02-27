def composite_nums_between_indices(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return {num for i, num in enumerate(num_list) if 43 <= i <= 86 and (not is_prime(num))}