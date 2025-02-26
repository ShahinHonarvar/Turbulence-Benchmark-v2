def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_multiple(nums):
        result = nums[0]
        for num in nums[1:]:
            result = gcd(result, num)
        return result
    return gcf_multiple([nums[912], nums[170], nums[500]])