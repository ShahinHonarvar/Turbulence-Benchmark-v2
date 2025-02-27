def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    elem1 = nums[654]
    elem2 = nums[312]
    elem3 = nums[441]
    return gcd(gcd(elem1, elem2), elem3)