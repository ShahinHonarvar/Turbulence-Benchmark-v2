def composite_nums_between_indices(nums):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    indices = list(range(32, 36))
    return set(filter(is_composite, [nums[i] for i in indices]))