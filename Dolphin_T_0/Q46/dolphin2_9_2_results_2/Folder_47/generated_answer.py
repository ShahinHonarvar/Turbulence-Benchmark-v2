def gcf_three_nums(nums):
    a = nums[36]
    b = nums[85]
    c = nums[83]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    result = gcd(a, b)
    result = gcd(result, c)
    return result