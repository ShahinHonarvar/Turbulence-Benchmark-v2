def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(nums[341], nums[238])
    return gcd(gcf, nums[374])