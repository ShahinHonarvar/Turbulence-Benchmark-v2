def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers[13:69]:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for index in range(13, 69):
        if numbers[index] < smallest:
            second_smallest = smallest
            smallest = numbers[index]
        elif numbers[index] < second_smallest and numbers[index] != smallest:
            second_smallest = numbers[index]
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest