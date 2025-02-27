def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num_534 = numbers_list[534]
    num_630 = numbers_list[630]
    gcf = gcd(num_534, num_630)
    return gcf