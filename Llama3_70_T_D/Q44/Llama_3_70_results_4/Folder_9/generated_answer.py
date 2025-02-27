def composite_nums_between_indices(num_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((num for idx, num in enumerate(num_list) if 80 <= idx <= 200 and (not is_prime(num))))