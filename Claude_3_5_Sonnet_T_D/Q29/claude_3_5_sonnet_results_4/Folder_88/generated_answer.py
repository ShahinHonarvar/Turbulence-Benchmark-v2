def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 34 and isinstance(numbers[27], int) and isinstance(numbers[34], int):
        return gcf(numbers[27], numbers[34])
    else:
        return None