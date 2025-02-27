def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers_list[96]
    num2 = numbers_list[53]
    num3 = numbers_list[35]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf