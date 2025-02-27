def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    second_smallest = None
    smallest = float('inf')
    for i in range(80, 201):
        if numbers[i] < smallest:
            second_smallest = smallest
            smallest = numbers[i]
        elif numbers[i] < second_smallest or second_smallest is None:
            second_smallest = numbers[i]
    return second_smallest