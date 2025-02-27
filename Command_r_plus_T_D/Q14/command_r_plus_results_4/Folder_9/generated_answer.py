def find_second_smallest_num(numbers: list[int]) -> int:
    second_smallest = None
    min_val = float('inf')
    second_min_val = float('inf')
    for i in range(70, 201):
        if numbers[i] < min_val:
            second_smallest = min_val
            min_val = numbers[i]
        elif numbers[i] < second_min_val and numbers[i] != min_val:
            second_min_val = numbers[i]
    if second_smallest is not None:
        return second_smallest
    else:
        return None