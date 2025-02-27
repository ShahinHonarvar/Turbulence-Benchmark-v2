def gcf_three_nums(list_of_nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(list_of_nums[90], list_of_nums[54]), list_of_nums[96])