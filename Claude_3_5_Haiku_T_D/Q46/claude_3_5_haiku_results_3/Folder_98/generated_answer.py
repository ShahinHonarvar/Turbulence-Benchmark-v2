def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_multiple(nums):
        result = nums[0]
        for num in nums[1:]:
            result = gcd(result, num)
        return result
    selected_nums = [nums[8], nums[2], nums[1]]
    return gcd_multiple(selected_nums)