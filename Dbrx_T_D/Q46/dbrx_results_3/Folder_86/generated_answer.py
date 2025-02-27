def gcf_three_nums(nums):

    def gcd(a, b):
        return gcd(b, a % b) if b else a
    num1, num2, num3 = (nums[341], nums[238], nums[374])
    return gcd(num1, gcd(num2, num3))