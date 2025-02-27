def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num76 = numbers_list[75]
    num64 = numbers_list[63]
    num28 = numbers_list[27]
    gcf = gcd(gcd(num76, num64), num28)
    return gcf