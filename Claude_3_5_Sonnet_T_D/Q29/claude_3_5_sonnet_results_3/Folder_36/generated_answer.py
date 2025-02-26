def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > max(429, 289):
        return calculate_gcf(numbers[429], numbers[289])
    else:
        return None