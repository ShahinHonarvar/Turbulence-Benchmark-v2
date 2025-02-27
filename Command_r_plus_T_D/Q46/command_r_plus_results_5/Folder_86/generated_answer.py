def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[340]
    num2 = numbers_list[237]
    num3 = numbers_list[373]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf