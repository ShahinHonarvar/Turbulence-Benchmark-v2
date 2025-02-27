def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[76]
    num2 = numbers_list[64]
    num3 = numbers_list[28]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf