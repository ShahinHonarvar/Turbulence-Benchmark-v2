def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num0 = numbers_list[0]
    num8 = numbers_list[8]
    num3 = numbers_list[3]
    gcf_0_8 = gcd(num0, num8)
    gcf_0_8_3 = gcd(gcf_0_8, num3)
    return gcf_0_8_3