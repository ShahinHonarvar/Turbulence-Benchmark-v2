def gcf_three_nums(nums):
    a = nums[90]
    b = nums[54]
    c = nums[96]
    i = 1
    while i <= a or i <= b or i <= c:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factor = i
        i += 1
    return factor