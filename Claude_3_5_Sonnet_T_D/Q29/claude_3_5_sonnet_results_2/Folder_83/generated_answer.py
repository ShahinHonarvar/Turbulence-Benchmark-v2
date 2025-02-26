def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 20 and isinstance(numbers[17], int) and isinstance(numbers[20], int) and (numbers[17] > 0) and (numbers[20] > 0):
        return gcf(numbers[17], numbers[20])
    else:
        return None