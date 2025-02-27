def gcf_three_nums(num_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (num_list[144], num_list[182], num_list[769])
    gcf = gcd(gcd(num1, num2), num3)
    return gcf