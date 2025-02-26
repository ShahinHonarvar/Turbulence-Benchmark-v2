def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 10:
        return None
    num1 = numbers[0]
    num2 = numbers[9]
    return gcd(num1, num2)