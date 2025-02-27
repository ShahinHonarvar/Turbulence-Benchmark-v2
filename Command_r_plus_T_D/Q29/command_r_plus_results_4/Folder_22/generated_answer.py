def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcf_calculator(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    return gcf_calculator(numbers_list[24], numbers_list[68])