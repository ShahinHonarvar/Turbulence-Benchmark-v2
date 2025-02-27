def find_second_smallest_num(numbers: list[int]) -> int:
    smallest_two = [float('inf'), float('inf')]
    for idx in range(10):
        if numbers[idx] < smallest_two[0]:
            smallest_two[1] = smallest_two[0]
            smallest_two[0] = numbers[idx]
        elif numbers[idx] < smallest_two[1] and numbers[idx] != smallest_two[0]:
            smallest_two[1] = numbers[idx]
    return smallest_two[1] if smallest_two[1] != float('inf') else None