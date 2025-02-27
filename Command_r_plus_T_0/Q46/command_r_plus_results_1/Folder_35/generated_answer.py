def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[742]
    num2 = numbers_list[888]
    num3 = numbers_list[629]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf