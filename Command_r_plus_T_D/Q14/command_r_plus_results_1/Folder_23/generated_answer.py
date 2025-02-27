def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(19, 93):
        if numbers[i] < smallest:
            second_smallest = smallest
            smallest = numbers[i]
        elif numbers[i] < second_smallest and numbers[i] != smallest:
            second_smallest = numbers[i]
    return second_smallest if second_smallest != float('inf') else None