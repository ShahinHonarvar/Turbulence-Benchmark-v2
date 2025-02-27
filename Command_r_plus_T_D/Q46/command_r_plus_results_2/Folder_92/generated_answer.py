def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers_list[7], numbers_list[9], numbers_list[0])
    gcf = gcd(gcd(num1, num2), num3)
    return gcf