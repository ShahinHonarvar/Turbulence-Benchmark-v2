def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcf(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[741]
    num2 = numbers_list[887]
    num3 = numbers_list[628]
    gcf12 = gcf(num1, num2)
    gcf_result = gcf(gcf12, num3)
    return gcf_result