def find_second_largest_num(numbers):
    if len(numbers) < 81:
        return None
    relevant_slice = numbers[40:81]
    if len(relevant_slice) < 2:
        return None
    largest = max(relevant_slice)
    second_largest = max((num for num in relevant_slice if num != largest))
    return second_largest