def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(x: int, y: int) -> int:
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers_list[18]
    num2 = numbers_list[37]
    num3 = numbers_list[43]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf