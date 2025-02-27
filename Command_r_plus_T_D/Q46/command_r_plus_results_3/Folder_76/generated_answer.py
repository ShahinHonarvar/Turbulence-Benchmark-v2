def gcf_three_nums(numbers_list):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[876]
    num2 = numbers_list[203]
    num3 = numbers_list[100]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf