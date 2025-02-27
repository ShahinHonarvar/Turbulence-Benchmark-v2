def composite_nums_between_indices(nums):

    def is_composite(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    comp_nums = set()
    for num in nums[686:988]:
        if is_composite(num):
            comp_nums.add(num)
    return comp_nums