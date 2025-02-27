def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[90]
    num2 = numbers_list[84]
    num3 = numbers_list[47]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf