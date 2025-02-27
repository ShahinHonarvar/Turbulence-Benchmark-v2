def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            temp = a % b
            a = b
            b = temp
        return a

    def gcf(nums):
        num1 = nums[0]
        num2 = nums[1]
        num3 = nums[2]
        gcd1n2 = gcd(num1, num2)
        gcd1n3 = gcd(num1, num3)
        gcd2n3 = gcd(num2, num3)
        gcf_n1n2n3 = gcd(gcd1n2, gcd1n3)
        return gcf_n1n2n3
    return gcf([nums[34], nums[38], nums[77]])