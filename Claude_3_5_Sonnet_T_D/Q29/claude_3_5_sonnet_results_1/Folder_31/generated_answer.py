def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 96:
        return None
    num1 = numbers[87]
    num2 = numbers[95]
    return gcd(num1, num2)