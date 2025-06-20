def composite_nums_between_indices(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((num for i, num in enumerate(nums) if 30 <= i <= 48 and (not is_prime(num))))