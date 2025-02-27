def gcf_two_nums(nums):
    x = nums[28]
    y = nums[20]
    common_divs = []
    for i in range(1, x + 1):
        if x % i == 0 and y % i == 0:
            common_divs.append(i)
    return max(common_divs)