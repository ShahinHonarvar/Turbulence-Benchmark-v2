def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (numbers_list[41], numbers_list[69], numbers_list[28])
    gcf = gcd(a, gcd(b, c))
    return gcf