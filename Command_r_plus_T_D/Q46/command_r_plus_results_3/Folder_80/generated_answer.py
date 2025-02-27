def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(x: int, y: int) -> int:
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers_list[13]
    num2 = numbers_list[76]
    num3 = numbers_list[44]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf