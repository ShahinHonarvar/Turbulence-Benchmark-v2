def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[412]
    num2 = numbers_list[932]
    num3 = numbers_list[337]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf