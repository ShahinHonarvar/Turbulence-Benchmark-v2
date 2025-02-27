def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    second_smallest = None
    smallest = numbers[608]
    for num in numbers[608:610]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or (num < second_smallest and num != smallest):
            second_smallest = num
    return second_smallest