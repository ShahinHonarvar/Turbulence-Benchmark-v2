def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 53 and isinstance(numbers[49], int) and isinstance(numbers[53], int):
        return calculate_gcf(numbers[49], numbers[53])
    else:
        return None