def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    first_num = nums[145]
    second_num = nums[183]
    third_num = nums[770]
    return gcd(first_num, gcd(second_num, third_num))