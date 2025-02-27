def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num991 = numbers_list[991]
    num244 = numbers_list[244]
    num974 = numbers_list[974]
    gcf_991_244 = gcd(num991, num244)
    gcf_244_974 = gcd(num244, num974)
    return gcd(gcf_991_244, gcf_244_974)