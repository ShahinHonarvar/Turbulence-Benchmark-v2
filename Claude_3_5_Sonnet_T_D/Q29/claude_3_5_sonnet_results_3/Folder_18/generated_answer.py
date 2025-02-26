def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > max(872, 219):
        num1 = numbers[872]
        num2 = numbers[219]
        return calculate_gcf(num1, num2)
    else:
        return None