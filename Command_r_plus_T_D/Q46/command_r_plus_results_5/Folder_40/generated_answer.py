def gcf_three_nums(numbers: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[1]
    num6 = numbers[6]
    num8 = numbers[8]
    gcf = gcd(num1, num6)
    gcf = gcd(gcf, num8)
    return gcf