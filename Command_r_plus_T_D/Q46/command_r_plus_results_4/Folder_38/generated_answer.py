def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcf(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[14]
    num2 = numbers_list[21]
    num3 = numbers_list[17]
    gcf_num1_num2 = gcf(num1, num2)
    gcf_three_nums = gcf(gcf_num1_num2, num3)
    return gcf_three_nums