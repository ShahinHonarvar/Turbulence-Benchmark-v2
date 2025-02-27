def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    x, y = (nums[534], nums[630])
    return gcd(x, y)