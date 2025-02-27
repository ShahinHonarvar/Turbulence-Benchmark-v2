def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcf(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[4]
    num2 = numbers_list[1]
    num3 = numbers_list[7]
    gcf1_2 = gcf(num1, num2)
    gcf_result = gcf(gcf1_2, num3)
    return gcf_result