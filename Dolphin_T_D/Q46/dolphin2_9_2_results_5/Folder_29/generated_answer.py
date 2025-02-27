def gcf_three_nums(nums):
    a = nums[22]
    b = nums[97]
    c = nums[64]
    i = 1
    while i <= a or i <= b or i <= c:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf