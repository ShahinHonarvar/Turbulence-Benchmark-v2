def composite_nums_between_indices(nums):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    comp_nums = set()
    for i in range(len(nums)):
        if 0 <= i <= 2 and is_composite(nums[i]):
            comp_nums.add(nums[i])
    return comp_nums