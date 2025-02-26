def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 68:
        return None
    num1 = numbers[28]
    num2 = numbers[67]
    return calculate_gcf(num1, num2)