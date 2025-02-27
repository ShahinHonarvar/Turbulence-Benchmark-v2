def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcf_calculator(num1: int, num2: int) -> int:
        while num2:
            num1, num2 = (num2, num1 % num2)
        return num1
    num1 = numbers_list[84]
    num2 = numbers_list[21]
    return gcf_calculator(num1, num2)