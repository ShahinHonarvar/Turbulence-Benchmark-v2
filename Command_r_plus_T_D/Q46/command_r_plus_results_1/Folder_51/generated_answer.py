def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[21]
    num2 = numbers_list[69]
    num3 = numbers_list[41]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf