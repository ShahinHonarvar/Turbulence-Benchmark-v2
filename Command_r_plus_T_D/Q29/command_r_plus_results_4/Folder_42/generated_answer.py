def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcf_calculation(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    return gcf_calculation(numbers_list[90], numbers_list[84])