def gcf_three_nums(nums):
    num1 = nums[10]
    num2 = nums[55]
    num3 = nums[36]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcd = gcf(num1, num2)
    gcf_final = gcf(gcd, num3)
    return gcf_final