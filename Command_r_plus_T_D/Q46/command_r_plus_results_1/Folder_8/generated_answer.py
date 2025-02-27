def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcf(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_99 = numbers_list[99]
    num_28 = numbers_list[28]
    num_53 = numbers_list[53]
    gcf_99_28 = gcf(num_99, num_28)
    gcf_53 = gcf(gcf_99_28, num_53)
    return gcf_53