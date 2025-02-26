def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 86:
        return None
    num1 = numbers[85]
    num2 = numbers[51]
    return gcd(num1, num2)