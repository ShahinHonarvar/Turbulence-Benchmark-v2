def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers_list[7], numbers_list[6], numbers_list[8])
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf