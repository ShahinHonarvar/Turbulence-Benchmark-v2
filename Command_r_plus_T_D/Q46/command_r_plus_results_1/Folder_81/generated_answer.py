def gcf_three_nums(num_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = num_list[20]
    num2 = num_list[17]
    num3 = num_list[28]
    gcf = gcd(gcd(num1, num2), num3)
    return gcf