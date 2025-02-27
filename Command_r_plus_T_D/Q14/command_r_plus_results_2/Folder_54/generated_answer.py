def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(68, 87):
        if numbers[i] < second_smallest and numbers[i] > smallest:
            second_smallest = numbers[i]
        elif numbers[i] < smallest:
            smallest = numbers[i]
    if second_smallest == float('inf'):
        return None
    else:
        return second_smallest