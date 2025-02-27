def find_second_smallest_num(numbers):
    numbers_slice = numbers[6:9]
    if len(numbers_slice) < 2:
        return None
    smallest = min(numbers_slice)
    numbers_slice.remove(smallest)
    return min(numbers_slice)