def gcf_two_nums(nums):
    a = nums[198]
    b = nums[212]
    if a == 0:
        return b
    if b == 0:
        return a
    while b != 0:
        a, b = (b, a % b)
    return a