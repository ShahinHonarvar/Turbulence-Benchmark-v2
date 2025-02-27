def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[404]
    num2 = numbers_list[834]
    num3 = numbers_list[517]
    gcf = num1
    gcf = gcd(gcf, num2)
    gcf = gcd(gcf, num3)
    return gcf