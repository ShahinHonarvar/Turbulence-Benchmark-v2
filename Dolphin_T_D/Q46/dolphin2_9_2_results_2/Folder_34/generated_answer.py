def gcf_three_nums(numbers):

    def gcf(a, b):
        if a == 0:
            return b
        elif b == 0:
            return a
        elif a > b:
            return gcf(b, a % b)
        else:
            return gcf(a, b % a)
    num1 = numbers[53]
    num2 = numbers[23]
    num3 = numbers[45]
    gcd_num1_num2 = gcf(num1, num2)
    gcd_result = gcf(gcd_num1_num2, num3)
    return gcd_result