def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[90]
    num2 = numbers_list[41]
    num3 = numbers_list[95]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf