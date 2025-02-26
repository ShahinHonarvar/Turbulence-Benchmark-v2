def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 50:
        return None
    num1 = numbers[49]
    num2 = numbers[31]
    return gcd(num1, num2)