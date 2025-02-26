def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 8:
        return calculate_gcf(numbers[8], numbers[3])
    else:
        return None