def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 99 and isinstance(numbers[43], int) and isinstance(numbers[99], int):
        return calculate_gcf(numbers[43], numbers[99])
    else:
        return None