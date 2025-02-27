def gcf_three_nums(nums):
    a, b, c = (nums[74], nums[51], nums[27])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a * (abs(nums[74] // a) * abs(nums[51] // a) * abs(nums[27] // a))