def gcf_two_nums(nums):
    if len(nums) < 95:
        return 'Error: list does not have enough elements.'
    else:
        a = nums[19]
        b = nums[94]
        i = min(a, b)
        while i > 1:
            if a % i == 0 and b % i == 0:
                return i
            i -= 1
        return 1