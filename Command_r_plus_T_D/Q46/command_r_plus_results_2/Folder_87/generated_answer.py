def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcf_two_nums(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[74]
    num2 = numbers_list[60]
    num3 = numbers_list[28]
    gcf12 = gcf_two_nums(num1, num2)
    gcf123 = gcf_two_nums(gcf12, num3)
    return gcf123