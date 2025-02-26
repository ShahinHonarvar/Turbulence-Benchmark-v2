def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 9:
        return None
    a = nums[4]
    b = nums[0]
    c = nums[8]
    result = gcd(a, b)
    result = gcd(result, c)
    return result