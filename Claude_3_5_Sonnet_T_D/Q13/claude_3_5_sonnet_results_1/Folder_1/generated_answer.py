def find_second_largest_num(numbers):
    if len(numbers) < 73:
        return None
    relevant_slice = numbers[31:73]
    if len(relevant_slice) < 2:
        return None
    largest = max(relevant_slice)
    second_largest = max((num for num in relevant_slice if num != largest))
    return second_largest