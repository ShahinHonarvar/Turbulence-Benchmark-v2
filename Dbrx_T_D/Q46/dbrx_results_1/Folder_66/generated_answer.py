def gcf_three_nums(numbers):
    if len(numbers) < 3:
        return None

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[92]
    num2 = numbers[69]
    num3 = numbers[95]
    return gcd(num1, gcd(num2, num3))