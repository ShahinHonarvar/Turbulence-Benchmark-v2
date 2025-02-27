def find_second_smallest_num(numbers: list[int]) -> int:
    second_smallest = None
    smallest = float('inf')
    for i in range(1, 9):
        if numbers[i] < smallest:
            second_smallest = smallest
            smallest = numbers[i]
        elif numbers[i] < second_smallest and numbers[i] != smallest:
            second_smallest = numbers[i]
    return second_smallest