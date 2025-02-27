def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[404]
    num2 = numbers_list[834]
    num3 = numbers_list[517]
    gcf = gcd(gcd(num1, num2), num3)
    return gcf