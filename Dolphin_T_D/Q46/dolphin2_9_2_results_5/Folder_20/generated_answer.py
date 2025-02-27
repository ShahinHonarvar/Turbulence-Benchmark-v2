def gcd(a, b):
    while b > 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    nums = [lst[29], lst[53], lst[42]]
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result