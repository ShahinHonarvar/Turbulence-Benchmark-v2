def gcf_three_nums(numbers: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[9]
    num2 = numbers[6]
    num3 = numbers[2]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf