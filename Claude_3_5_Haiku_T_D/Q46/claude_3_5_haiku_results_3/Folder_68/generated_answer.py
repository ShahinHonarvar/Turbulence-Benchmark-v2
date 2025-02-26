def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_multiple(nums):
        result = nums[0]
        for num in nums[1:]:
            result = gcd(result, num)
        return result
    return gcd_multiple([numbers[4], numbers[1], numbers[7]])