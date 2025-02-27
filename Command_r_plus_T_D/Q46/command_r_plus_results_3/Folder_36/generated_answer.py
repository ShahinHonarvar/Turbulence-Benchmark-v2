def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num427 = numbers_list[426] if len(numbers_list) > 426 else 0
    num761 = numbers_list[760] if len(numbers_list) > 760 else 0
    num148 = numbers_list[147] if len(numbers_list) > 147 else 0
    gcf = gcd(num427, num761)
    gcf = gcd(gcf, num148)
    return gcf