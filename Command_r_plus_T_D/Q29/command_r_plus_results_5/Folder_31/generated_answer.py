def gcf_two_nums(num_list: list[int]) -> int:

    def gcf(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    return gcf(num_list[86], num_list[94])