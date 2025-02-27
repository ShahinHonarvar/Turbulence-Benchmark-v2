def gcf_two_nums(nums):

    def gcd(a, b):
        if a == 0:
            return b
        elif b == 0:
            return a
        elif a == b:
            return a
        elif a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)
    return gcd(nums[872], nums[219])