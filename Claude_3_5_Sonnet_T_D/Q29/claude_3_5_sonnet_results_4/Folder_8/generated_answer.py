def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 70:
        return None
    num1 = numbers[69]
    num2 = numbers[41]
    return gcd(num1, num2)