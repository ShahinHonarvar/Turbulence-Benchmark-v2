def find_second_largest_num(numbers):
    if len(numbers) < 539:
        return None
    num_slice = numbers[527:539]
    num_slice.sort(reverse=True)
    if len(num_slice) < 2:
        return None
    return num_slice[1]