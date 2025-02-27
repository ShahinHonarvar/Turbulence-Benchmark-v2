def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[31]
    num2 = numbers_list[69]
    num3 = numbers_list[40]
    gcf_1_2 = gcd(num1, num2)
    gcf_3 = gcd(gcf_1_2, num3)
    return gcf_3