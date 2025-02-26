def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 93:
        return None
    num1 = numbers[56]
    num2 = numbers[92]
    return gcd(num1, num2)