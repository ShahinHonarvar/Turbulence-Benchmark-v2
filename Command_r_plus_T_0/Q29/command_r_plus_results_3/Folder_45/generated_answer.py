def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcf(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_47 = numbers_list[46]
    num_97 = numbers_list[96]
    return gcf(num_47, num_97)