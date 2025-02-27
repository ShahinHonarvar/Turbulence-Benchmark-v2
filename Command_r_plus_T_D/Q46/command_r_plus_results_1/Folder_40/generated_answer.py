def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[1]
    num6 = numbers_list[6]
    num8 = numbers_list[8]
    gcf = gcd(num1, gcd(num6, num8))
    return gcf