def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcf_calculator(num1: int, num2: int) -> int:
        while num2:
            num1, num2 = (num2, num1 % num2)
        return num1
    num90 = numbers_list[90]
    num54 = numbers_list[54]
    return gcf_calculator(num90, num54)