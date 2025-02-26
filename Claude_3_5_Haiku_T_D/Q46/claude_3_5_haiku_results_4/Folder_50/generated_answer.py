def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_three(x, y, z):
        first_two = gcd(x, y)
        return gcd(first_two, z)
    return gcf_three(nums[20], nums[35], nums[74])