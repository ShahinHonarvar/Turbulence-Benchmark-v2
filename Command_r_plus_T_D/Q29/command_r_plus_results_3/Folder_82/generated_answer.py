def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcf_calculation(num1: int, num2: int) -> int:
        while num2:
            num1, num2 = (num2, num1 % num2)
        return num1
    return gcf_calculation(numbers_list[33], numbers_list[72])