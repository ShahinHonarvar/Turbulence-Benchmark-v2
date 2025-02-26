def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 67:
        return None
    num1 = numbers[13]
    num2 = numbers[66]
    return gcd(num1, num2)