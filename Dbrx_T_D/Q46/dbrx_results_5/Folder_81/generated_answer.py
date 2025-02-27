def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    element1 = nums[20]
    element2 = nums[17]
    element3 = nums[28]
    return gcd(element1, gcd(element2, element3))