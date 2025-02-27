def gcf_three_nums(numbers: list[int]) -> int:

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num0 = numbers[0]
    num8 = numbers[8]
    num3 = numbers[3]
    gcf = gcd(num0, num8)
    gcf = gcd(gcf, num3)
    return gcf