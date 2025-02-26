def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 92:
        return None
    num1 = numbers[91]
    num2 = numbers[45]
    return gcf(num1, num2)