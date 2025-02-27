def gcf_two_nums(nums):
    a = nums[21]
    b = nums[17]
    i = 1
    while i <= a or i <= b:
        if a % i == 0 and b % i == 0:
            gcf = i
        else:
            i += 1
    return gcf