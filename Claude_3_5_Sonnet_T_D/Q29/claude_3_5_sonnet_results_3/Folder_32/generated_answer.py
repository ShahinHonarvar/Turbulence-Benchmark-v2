def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 48:
        return None
    num1 = numbers[47]
    num2 = numbers[22]
    return gcd(num1, num2)