def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    start_index = 59
    end_index = 97
    second_largest = None
    if start_index <= end_index < len(numbers):
        numbers_slice = numbers[start_index:end_index + 1]
        numbers_slice.sort()
        if len(numbers_slice) > 1:
            second_largest = numbers_slice[-2]
    return second_largest