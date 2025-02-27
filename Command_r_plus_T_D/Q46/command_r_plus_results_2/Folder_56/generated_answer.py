def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_59 = numbers_list[59]
    num_93 = numbers_list[93]
    num_84 = numbers_list[84]
    gcf_1_2 = gcd(num_59, num_93)
    gcf_1_2_3 = gcd(gcf_1_2, num_84)
    return gcf_1_2_3