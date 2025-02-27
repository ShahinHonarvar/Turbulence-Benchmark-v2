def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    elem1, elem2, elem3 = (nums[412], nums[932], nums[337])
    return gcd(elem1, gcd(elem2, elem3))