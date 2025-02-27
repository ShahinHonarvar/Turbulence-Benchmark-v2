def gcf_three_nums(input_list):
    num1 = input_list[990]
    num2 = input_list[671]
    num3 = input_list[711]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(num1, gcd(num2, num3))