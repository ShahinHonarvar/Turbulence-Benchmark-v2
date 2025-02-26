def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 47 and len(numbers) > 10:
        num1 = numbers[47]
        num2 = numbers[10]
        return gcd(num1, num2)
    else:
        return None