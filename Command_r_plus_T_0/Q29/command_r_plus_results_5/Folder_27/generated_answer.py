def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num15 = numbers_list[15]
    num40 = numbers_list[40]
    gcf = gcd(num15, num40)
    return gcf