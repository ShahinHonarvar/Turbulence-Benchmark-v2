def gcf_three_nums(nums):
    a = nums[693]
    b = nums[331]
    c = nums[668]
    gcf = 1
    for i in range(2, min([a, b, c]) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf