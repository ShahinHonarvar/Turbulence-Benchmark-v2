def gcf_three_nums(numbers_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[0]
    num2 = numbers_list[8]
    num3 = numbers_list[3]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf