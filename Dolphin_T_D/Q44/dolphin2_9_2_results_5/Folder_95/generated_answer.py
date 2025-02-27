def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return set((num for index, num in enumerate(nums) if 26 <= index <= 52 and is_composite(num)))