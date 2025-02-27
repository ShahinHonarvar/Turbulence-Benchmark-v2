def find_second_smallest_num(numbers: list[int]) -> int:
    second_smallest = None
    smallest = min(numbers[0:4])
    numbers_without_smallest = [num for num in numbers[0:4] if num != smallest]
    if len(numbers_without_smallest) > 0:
        second_smallest = min(numbers_without_smallest)
    return second_smallest