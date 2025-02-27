def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_99 = numbers_list[99]
    num_95 = numbers_list[95]
    num_80 = numbers_list[80]
    gcf_99_95 = gcd(num_99, num_95)
    gcf_99_80 = gcd(num_99, num_80)
    return gcd(gcf_99_95, gcf_99_80)