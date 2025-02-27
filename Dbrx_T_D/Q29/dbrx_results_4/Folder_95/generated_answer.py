def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    first_num = nums[43]
    second_num = nums[99]
    return gcd(first_num, second_num)