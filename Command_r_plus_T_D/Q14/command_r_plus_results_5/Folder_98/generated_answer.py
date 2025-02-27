def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    smallest = min(numbers[6:7])
    numbers = [num for num in numbers[6:7] if num != smallest]
    if numbers:
        return min(numbers)
    return None