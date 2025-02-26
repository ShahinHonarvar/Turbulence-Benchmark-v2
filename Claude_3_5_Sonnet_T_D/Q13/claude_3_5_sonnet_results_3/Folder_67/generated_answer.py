def find_second_largest_num(numbers):
    sublist = numbers[22:51]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = max((num for num in sublist if num != largest))
    return second_largest