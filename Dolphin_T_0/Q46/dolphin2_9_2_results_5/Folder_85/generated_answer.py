def gcf_three_nums(nums):
    if len(nums) >= 50:
        a = nums[49]
        if len(nums) >= 47:
            b = nums[46]
            if len(nums) >= 14:
                c = nums[13]
                i = min(a, b, c)
                while True:
                    if a % i == 0 and b % i == 0 and (c % i == 0):
                        return i
                    i -= 1
    return -1