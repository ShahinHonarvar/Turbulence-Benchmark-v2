def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[19]
    num2 = numbers_list[94]
    num3 = numbers_list[78]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf