def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 307 and isinstance(numbers[184], int) and isinstance(numbers[307], int):
        return calculate_gcf(numbers[184], numbers[307])
    else:
        return None