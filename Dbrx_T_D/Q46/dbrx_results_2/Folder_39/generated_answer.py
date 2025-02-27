def gcf_three_nums(numbers: list[int]) -> int:

    def gcd(a: int, b: int) -> int:
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[85], numbers[36], numbers[54])
    return gcd(gcd(num1, num2), num3)