def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 27 and isinstance(numbers[23], int) and isinstance(numbers[27], int):
        return calculate_gcf(numbers[23], numbers[27])
    else:
        return None