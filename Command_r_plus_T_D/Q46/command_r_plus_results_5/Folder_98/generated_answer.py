def gcf_three_nums(numbers: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[8], numbers[2], numbers[1])
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf