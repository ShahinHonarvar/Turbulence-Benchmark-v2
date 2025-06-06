def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[85]
    num2 = numbers_list[36]
    num3 = numbers_list[54]
    gcf_1_2 = gcd(num1, num2)
    gcf_1_2_3 = gcd(gcf_1_2, num3)
    return gcf_1_2_3