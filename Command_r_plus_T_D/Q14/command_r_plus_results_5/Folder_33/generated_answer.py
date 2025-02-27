def find_second_smallest_num(numbers: list[int]) -> int:
    second_smallest = None
    smallest = None
    for i in range(262, 747):
        if smallest is None or numbers[i] < smallest:
            second_smallest = smallest
            smallest = numbers[i]
        elif second_smallest is None or (numbers[i] < second_smallest and numbers[i] != smallest):
            second_smallest = numbers[i]
    return second_smallest