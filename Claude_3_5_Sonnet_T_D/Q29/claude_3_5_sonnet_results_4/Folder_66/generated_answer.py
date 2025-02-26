def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 90 or not all((isinstance(num, int) and num > 0 for num in numbers)):
        return None
    num1 = numbers[86]
    num2 = numbers[89]
    return gcd(num1, num2)