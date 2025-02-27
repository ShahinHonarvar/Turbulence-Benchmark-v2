def gcf_three_nums(num_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[4]
    num2 = num_list[1]
    num3 = num_list[7]
    gcf = gcd(gcd(num1, num2), num3)
    return gcf