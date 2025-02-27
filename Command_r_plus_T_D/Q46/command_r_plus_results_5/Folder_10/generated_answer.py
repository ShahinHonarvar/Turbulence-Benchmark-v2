def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers_list[86], numbers_list[89], numbers_list[49])
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf