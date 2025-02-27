def gcf_two_nums(nums):
    if len(nums) != 2:
        raise ValueError('List must contain exactly two integers')
    gcd = nums[0]
    for i in range(1, len(nums)):
        gcd = gcd_two_nums_two_numbers(gcd, nums[i])
    return gcd

def gcd_two_nums_two_numbers(a, b):
    while b:
        a, b = (b, a % b)
    return a