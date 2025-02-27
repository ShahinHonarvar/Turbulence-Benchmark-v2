def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num15 = numbers_list[15]
    num51 = numbers_list[51]
    num76 = numbers_list[76]
    gcf = gcd(num15, num51)
    gcf = gcd(gcf, num76)
    return gcf