def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_56 = numbers_list[56]
    num_88 = numbers_list[88]
    num_51 = numbers_list[51]
    gcf_56_88 = gcd(num_56, num_88)
    gcf_56_88_51 = gcd(gcf_56_88, num_51)
    return gcf_56_88_51