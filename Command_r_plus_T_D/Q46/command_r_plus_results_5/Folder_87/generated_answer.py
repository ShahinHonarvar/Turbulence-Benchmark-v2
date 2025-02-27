def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcf(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num74 = numbers_list[73]
    num60 = numbers_list[59]
    num28 = numbers_list[27]
    gcf_num74_60 = gcf(num74, num60)
    gcf_num74_60_28 = gcf(gcf_num74_60, num28)
    return gcf_num74_60_28