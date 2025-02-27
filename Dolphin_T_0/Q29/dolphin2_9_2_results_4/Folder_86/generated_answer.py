def gcf_two_nums(nums_list):
    num1 = nums_list[793]
    num2 = nums_list[449]

    def gcd(num1, num2):
        while num2:
            num1, num2 = (num2, num1 % num2)
        return num1
    return gcd(num1, num2)