def gcf_three_nums(num_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[40]
    num2 = num_list[15]
    num3 = num_list[99]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf