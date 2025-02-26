def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 91 and len(numbers) > 45:
        num1 = numbers[91]
        num2 = numbers[45]
        return calculate_gcf(num1, num2)
    else:
        return None