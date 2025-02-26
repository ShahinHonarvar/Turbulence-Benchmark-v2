def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 78 and len(numbers) > 16:
        num1 = numbers[78]
        num2 = numbers[16]
        return gcd(num1, num2)
    else:
        return None