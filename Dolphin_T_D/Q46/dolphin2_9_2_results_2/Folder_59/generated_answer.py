def gcf_three_nums(num_list):
    num1 = num_list[7]
    num2 = num_list[6]
    num3 = num_list[8]

    def gcd(num1, num2, num3):
        while num2 != 0:
            num1, num2 = (num2, num1 % num2)
        return num1
    gcf = gcd(num1, num2, num3)
    return gcf