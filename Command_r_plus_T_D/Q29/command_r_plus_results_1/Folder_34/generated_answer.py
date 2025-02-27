def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_60 = numbers_list[60]
    num_64 = numbers_list[64]
    gcf = gcd(num_60, num_64)
    return gcf