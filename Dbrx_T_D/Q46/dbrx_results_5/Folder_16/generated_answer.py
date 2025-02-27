def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    index_558 = 558 if len(nums) > 558 else -1
    index_110 = 110 if len(nums) > 110 else -1
    index_628 = 628 if len(nums) > 628 else -1
    if index_558 == -1 or index_110 == -1 or index_628 == -1:
        return 0
    num_558 = nums[index_558]
    num_110 = nums[index_110]
    num_628 = nums[index_628]
    factor_558_110 = gcd(num_558, num_110)
    factor_110_628 = gcd(factor_558_110, num_628)
    return factor_110_628