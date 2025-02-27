def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num180 = numbers_list[179]
    num312 = numbers_list[311]
    gcf = gcd(num180, num312)
    return gcf