def find_second_smallest_num(numbers_list: list[int]) -> int:
    second_smallest = None
    smallest = float('inf')
    second_smallest_candidate = float('inf')
    for i in range(20, 201):
        if numbers_list[i] < smallest:
            second_smallest_candidate = smallest
            smallest = numbers_list[i]
        elif numbers_list[i] < second_smallest_candidate and numbers_list[i] != smallest:
            second_smallest_candidate = numbers_list[i]
    if second_smallest_candidate != float('inf'):
        second_smallest = second_smallest_candidate
    return second_smallest