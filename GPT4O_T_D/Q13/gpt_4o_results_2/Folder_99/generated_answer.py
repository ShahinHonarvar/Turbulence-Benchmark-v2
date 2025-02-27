def find_second_largest_num(numbers):
    if len(numbers) < 371:
        return None
    relevant_numbers = numbers[310:371]
    if len(relevant_numbers) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in relevant_numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None