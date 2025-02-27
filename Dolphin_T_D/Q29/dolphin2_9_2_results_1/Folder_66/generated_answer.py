def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def gcf_two_nums(nums):
    return gcd(nums[86], nums[89])