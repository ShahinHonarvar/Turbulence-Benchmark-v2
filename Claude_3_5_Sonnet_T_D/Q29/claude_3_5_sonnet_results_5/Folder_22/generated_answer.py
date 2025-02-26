def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 69:
        return None
    num1 = numbers[24]
    num2 = numbers[68]
    return gcd(num1, num2)