def gcf_three_nums(nums):
    nums = [nums[70], nums[41], nums[20]]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    result = nums[0]
    for i in nums[1:]:
        result = gcd(result, i)
    return result