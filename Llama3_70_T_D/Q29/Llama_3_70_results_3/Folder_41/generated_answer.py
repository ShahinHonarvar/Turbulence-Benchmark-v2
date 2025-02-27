def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    if len(numbers) < 28:
        raise ValueError('List must contain at least 28 elements')
    num1 = numbers[23]
    num2 = numbers[27]
    return calculate_gcf(num1, num2)