def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 96 and len(numbers) > 57:
        return calculate_gcf(numbers[96], numbers[57])
    else:
        return None