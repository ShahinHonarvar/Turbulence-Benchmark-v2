def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    idx1 = 33
    idx2 = 78
    idx3 = 93
    num1 = nums[idx1]
    num2 = nums[idx2]
    num3 = nums[idx3]
    gcf_1_2 = gcd(num1, num2)
    gcf = gcd(gcf_1_2, num3)
    return gcf