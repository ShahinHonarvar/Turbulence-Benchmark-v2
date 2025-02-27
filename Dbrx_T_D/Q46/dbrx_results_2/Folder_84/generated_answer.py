def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums = [numbers[694], numbers[709], numbers[913]]
    gcf = nums[0]
    for num in nums:
        gcf = gcd(gcf, num)
    return gcf