def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums = [numbers[16], numbers[87], numbers[95]]
    result = nums[0]
    for i in range(1, len(nums)):
        result = gcd(result, nums[i])
    return result