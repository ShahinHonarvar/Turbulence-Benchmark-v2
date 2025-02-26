def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start = 29
    end = min(51, len(nums) - 1)
    return set((num for i, num in enumerate(nums) if start <= i <= end and is_composite(num)))