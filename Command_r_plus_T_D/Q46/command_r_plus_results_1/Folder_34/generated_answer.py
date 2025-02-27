def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_53 = numbers_list[52]
    num_23 = numbers_list[22]
    num_45 = numbers_list[44]
    gcf = gcd(num_53, num_23)
    gcf = gcd(gcf, num_45)
    return gcf