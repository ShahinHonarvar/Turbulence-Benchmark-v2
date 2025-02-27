def find_second_smallest_num(numbers: list[int]) -> int:
    second_smallest = None
    smallest = None
    for i in range(70, 201):
        if smallest is None or numbers[i] < smallest:
            smallest, second_smallest = (numbers[i], smallest)
        elif second_smallest is None or numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest