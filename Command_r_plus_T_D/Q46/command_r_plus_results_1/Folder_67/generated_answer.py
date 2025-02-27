def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[70]
    num2 = numbers_list[41]
    num3 = numbers_list[20]
    gcf = gcd(gcd(num1, num2), num3)
    return gcf