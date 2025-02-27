def gcf_two_nums(nums):
    a = nums[2]
    b = nums[1]
    i = 1
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            gcf = i
        i += 1
    return gcf