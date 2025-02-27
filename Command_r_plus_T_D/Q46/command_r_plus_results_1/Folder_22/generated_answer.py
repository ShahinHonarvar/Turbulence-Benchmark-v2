def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(x: int, y: int) -> int:
        while y:
            x, y = (y, x % y)
        return x
    num1 = numbers_list[27]
    num2 = numbers_list[85]
    num3 = numbers_list[51]
    gcf = gcd(gcd(num1, num2), num3)
    return gcf