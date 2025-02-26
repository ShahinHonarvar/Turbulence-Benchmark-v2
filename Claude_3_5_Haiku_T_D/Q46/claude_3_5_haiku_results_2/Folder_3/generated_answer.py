def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_multiple(a, b, c):
        first_two = gcd(a, b)
        return gcd(first_two, c)
    return gcf_multiple(nums[31], nums[69], nums[40])