def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[13]
    num2 = numbers_list[76]
    num3 = numbers_list[44]
    gcf = num1
    gcf = gcd(gcf, num2)
    gcf = gcd(gcf, num3)
    return gcf