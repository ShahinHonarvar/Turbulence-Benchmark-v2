def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 10:
        return None
    num1 = numbers[8]
    num2 = numbers[9]
    return gcf(num1, num2)