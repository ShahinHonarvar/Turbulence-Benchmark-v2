def gcf_three_nums(nums):
    a = nums[16]
    b = nums[87]
    c = nums[95]
    i = 1
    while i > 0:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
            break
        i += 1
    return gcf