def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 582 and isinstance(numbers[129], int) and isinstance(numbers[582], int):
        return gcf(numbers[129], numbers[582])
    else:
        return None