def gcf_three_nums(nums):
    a = nums[0]
    b = nums[8]
    c = nums[3]
    gcf = a
    while b != 0 and c != 0:
        gcf = b
        b = a % b
        a = gcf
    return gcf