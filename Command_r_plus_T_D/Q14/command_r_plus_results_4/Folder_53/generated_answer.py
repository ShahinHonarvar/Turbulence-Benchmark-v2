def find_second_smallest_num(numbers: list[int]) -> int:
    second_smallest = None
    smallest = float('inf')
    for index in range(1, 101):
        if numbers[index] < smallest:
            second_smallest = smallest
            smallest = numbers[index]
        elif numbers[index] < second_smallest and numbers[index] != smallest:
            second_smallest = numbers[index]
    return second_smallest