def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcf_calculator(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[37]
    num2 = numbers_list[30]
    return gcf_calculator(num1, num2)