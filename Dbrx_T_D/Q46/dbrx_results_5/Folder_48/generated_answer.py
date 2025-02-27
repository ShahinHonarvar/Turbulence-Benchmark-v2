def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums = [numbers[654], numbers[312], numbers[441]]
    return gcd(nums[0], gcd(nums[1], nums[2]))