def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    second_smallest = None
    smallest = numbers[70]
    for index in range(70, 201):
        if numbers[index] < smallest:
            second_smallest = smallest
            smallest = numbers[index]
        elif numbers[index] < second_smallest or second_smallest is None:
            second_smallest = numbers[index]
    return second_smallest