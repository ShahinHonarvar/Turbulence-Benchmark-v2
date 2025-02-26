def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_three(a, b, c):
        first_two = gcd(a, b)
        return gcd(first_two, c)
    return gcf_three(nums[90], nums[54], nums[96])