def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 9 or len(numbers[6:9]) < 3:
        return None
    else:
        numbers_slice = numbers[6:9]
        numbers_slice.sort()
        return numbers_slice[1]