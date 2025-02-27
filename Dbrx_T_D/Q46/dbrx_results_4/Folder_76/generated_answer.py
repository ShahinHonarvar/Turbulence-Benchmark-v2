def gcd_two_numbers(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcd_two_numbers(gcd_two_numbers(nums[876], nums[203]), nums[100])