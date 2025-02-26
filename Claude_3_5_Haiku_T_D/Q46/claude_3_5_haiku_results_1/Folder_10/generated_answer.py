def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_list(nums):
        result = nums[0]
        for num in nums[1:]:
            result = gcd(result, num)
        return result
    return gcf_list([numbers[86], numbers[89], numbers[49]])