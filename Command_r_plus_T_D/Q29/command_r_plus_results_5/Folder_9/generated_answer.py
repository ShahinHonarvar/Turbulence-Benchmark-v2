def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num84 = numbers_list[83]
    num63 = numbers_list[62]
    gcf = gcd(num84, num63)
    return gcf