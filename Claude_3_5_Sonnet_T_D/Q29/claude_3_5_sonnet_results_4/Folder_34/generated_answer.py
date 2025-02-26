def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 64 and isinstance(numbers[60], int) and isinstance(numbers[64], int):
        return calculate_gcf(numbers[60], numbers[64])
    else:
        return None