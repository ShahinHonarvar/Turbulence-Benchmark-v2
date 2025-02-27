def composite_nums_between_indices(lst):

    def check_composite(n):
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime
    return set((num for num in lst[69:201] if not check_composite(num)))