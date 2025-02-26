def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 77:
        return None
    num1 = numbers[48]
    num2 = numbers[76]
    return calculate_gcf(num1, num2)