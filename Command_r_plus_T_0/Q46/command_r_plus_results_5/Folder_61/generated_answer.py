def gcf_three_nums(numbers_list: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers_list[1]
    num2 = numbers_list[2]
    num7 = numbers_list[7]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num7)
    return gcf