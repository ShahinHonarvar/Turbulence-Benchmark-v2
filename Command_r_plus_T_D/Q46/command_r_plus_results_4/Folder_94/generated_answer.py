def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_1 = numbers_list[56]
    num_2 = numbers_list[88]
    num_3 = numbers_list[51]
    gcf = gcd(num_1, num_2)
    gcf = gcd(gcf, num_3)
    return gcf