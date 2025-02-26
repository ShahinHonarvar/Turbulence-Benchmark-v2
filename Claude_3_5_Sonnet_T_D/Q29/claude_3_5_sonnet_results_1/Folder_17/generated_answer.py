def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 69 and len(numbers) > 40:
        num1 = numbers[69]
        num2 = numbers[40]
        return gcd(num1, num2)
    else:
        return None