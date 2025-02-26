def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) >= 10:
        return calculate_gcf(numbers[0], numbers[9])
    else:
        return None