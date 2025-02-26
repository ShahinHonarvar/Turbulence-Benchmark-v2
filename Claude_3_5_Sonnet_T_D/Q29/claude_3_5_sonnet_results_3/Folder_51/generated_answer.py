def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 84 and isinstance(numbers[46], int) and isinstance(numbers[84], int):
        return calculate_gcf(numbers[46], numbers[84])
    else:
        return None