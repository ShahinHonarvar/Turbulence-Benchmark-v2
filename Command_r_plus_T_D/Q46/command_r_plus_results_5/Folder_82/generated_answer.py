def gcf_three_nums(numbers_list: list[int]) -> int:
    num1, num2, num3 = (numbers_list[67], numbers_list[84], numbers_list[13])

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf