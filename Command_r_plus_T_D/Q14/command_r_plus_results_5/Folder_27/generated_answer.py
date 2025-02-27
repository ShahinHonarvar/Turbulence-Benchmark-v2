def find_second_smallest_num(numbers: list[int]) -> int:
    second_smallest = None
    numbers_slice = numbers[25:60]
    if len(numbers_slice) > 1:
        numbers_slice.sort()
        second_smallest = numbers_slice[1]
    return second_smallest