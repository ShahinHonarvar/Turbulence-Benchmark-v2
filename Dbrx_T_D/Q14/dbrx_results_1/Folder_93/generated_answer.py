def find_second_smallest_num(numbers):
    slice = numbers[75:89]
    if len(slice) < 2:
        return None
    else:
        first_smallest = min(slice)
        second_smallest = min((num for num in slice if num > first_smallest))
        return second_smallest