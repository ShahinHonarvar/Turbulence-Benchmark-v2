def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2 = (nums[894], nums[801])
    return gcd(num1, nums[801]) if num1 > num2 else gcd(num2, nums[894])