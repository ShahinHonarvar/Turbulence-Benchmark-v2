def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 45 and isinstance(numbers[23], int) and isinstance(numbers[45], int):
        return calculate_gcf(numbers[23], numbers[45])
    else:
        return None