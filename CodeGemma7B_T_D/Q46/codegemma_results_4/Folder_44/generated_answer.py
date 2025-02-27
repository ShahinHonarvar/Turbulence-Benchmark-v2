def gcf_three_nums(nums):
    num1 = nums[62]
    num2 = nums[96]
    num3 = nums[26]
    gcd = calculate_gcd(num1, num2)
    return calculate_gcd(gcd, num3)

def calculate_gcd(num1, num2):
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1