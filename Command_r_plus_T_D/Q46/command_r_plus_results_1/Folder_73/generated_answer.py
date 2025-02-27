def gcf_three_nums(num_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[90]
    num2 = num_list[84]
    num3 = num_list[47]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf