def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    first_num = nums[67]
    second_num = nums[84]
    third_num = nums[13]
    return gcd(gcd(first_num, second_num), third_num)