def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcf(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_1 = numbers_list[8]
    num_2 = numbers_list[9]
    return gcf(num_1, num_2)