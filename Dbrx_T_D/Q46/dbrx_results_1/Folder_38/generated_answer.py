def gcf_three_nums(numbers):

    def gcd(nums):
        result = numbers[0]
        for num in nums:
            while result % num != 0:
                result += numbers[0]
        return result
    nums_list = [numbers[14], numbers[21], numbers[17]]
    return gcd(nums_list)