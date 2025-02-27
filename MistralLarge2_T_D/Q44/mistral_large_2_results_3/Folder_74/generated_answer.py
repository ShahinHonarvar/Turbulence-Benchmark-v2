def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4 or (n % 2 == 0 and n > 2) or (n % 3 == 0 and n > 3):
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    return {num for i, num in enumerate(nums) if 42 <= i <= 68 and is_composite(num)}