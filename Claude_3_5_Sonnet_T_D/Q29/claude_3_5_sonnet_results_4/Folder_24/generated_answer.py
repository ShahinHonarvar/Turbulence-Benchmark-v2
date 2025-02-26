def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 84 and len(numbers) > 21:
        return calculate_gcf(numbers[84], numbers[21])
    else:
        return None