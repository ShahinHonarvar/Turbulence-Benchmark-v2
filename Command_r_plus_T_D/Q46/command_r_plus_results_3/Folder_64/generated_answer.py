def gcf_three_nums(numbers: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[0], numbers[8], numbers[3])
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf