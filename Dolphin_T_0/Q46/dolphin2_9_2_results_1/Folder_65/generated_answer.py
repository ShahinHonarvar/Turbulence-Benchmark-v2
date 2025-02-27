def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

def gcf_three_nums(nums):
    gcd_value = gcd(nums[18], nums[10])
    final_gcd = gcd(gcd_value, nums[76])
    return final_gcd