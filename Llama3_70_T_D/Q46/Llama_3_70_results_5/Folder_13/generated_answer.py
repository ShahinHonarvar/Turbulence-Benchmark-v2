def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    idx1, idx2, idx3 = (991, 244, 974)
    num1, num2, num3 = (nums[idx1], nums[idx2], nums[idx3])
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf