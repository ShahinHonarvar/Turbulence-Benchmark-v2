def gcf_two_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[84]
    num2 = numbers_list[13]
    gcf = gcd(num1, num2)
    return gcf