def gcf_two_nums(list_of_nums):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(list_of_nums[64], list_of_nums[28])