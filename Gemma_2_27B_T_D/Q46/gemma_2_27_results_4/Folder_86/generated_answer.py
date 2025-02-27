def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[341]
    b = nums[238]
    c = nums[374]
    return gcd(gcd(a, b), c)