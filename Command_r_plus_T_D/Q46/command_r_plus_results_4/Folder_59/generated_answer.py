def gcf_three_nums(num_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (num_list[7], num_list[6], num_list[8])
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf