def find_second_smallest_num(numbers):
    sublist = numbers[60:201]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    second_smallest = min((num for num in sublist if num != first_smallest))
    return second_smallest