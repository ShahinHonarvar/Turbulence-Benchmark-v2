def gcd_two_nums(n1, n2):
    if n1 == 0:
        return n2
    return gcd_two_nums(n2 % n1, n1)

def gcf_two_nums(nums):
    n1 = nums[66]
    n2 = nums[90]
    return gcd_two_nums(n1, n2)