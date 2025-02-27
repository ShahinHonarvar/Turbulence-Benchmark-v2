def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_64 = numbers_list[64]
    num_28 = numbers_list[28]
    gcf = gcd(num_64, num_28)
    return gcf