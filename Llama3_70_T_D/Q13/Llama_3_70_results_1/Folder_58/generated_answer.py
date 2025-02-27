def find_second_largest_num(numbers):
    if len(numbers) < 557:
        return None
    numbers_slice = sorted(numbers[209:557], reverse=True)
    if len(numbers_slice) < 2:
        return None
    return numbers_slice[1]