def gcf_three_nums(numbers: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[4]
    num2 = numbers[0]
    num3 = numbers[8]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf