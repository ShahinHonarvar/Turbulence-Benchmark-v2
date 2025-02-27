def find_second_largest_num(numbers):
    if len(numbers) < 81:
        return None
    numbers_slice = numbers[40:81]
    if len(numbers_slice) < 2:
        return None
    numbers_slice.sort(reverse=True)
    if len(numbers_slice) > 1:
        return numbers_slice[1]
    return None