def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 616:
        num1 = numbers[300]
        num2 = numbers[616]
        return calculate_gcf(num1, num2)
    else:
        return None