def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcf(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    return gcf(numbers_list[534], numbers_list[630])