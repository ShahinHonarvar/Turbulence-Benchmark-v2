def gcf_three_nums(list_of_nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(list_of_nums[31], list_of_nums[25]), list_of_nums[80])