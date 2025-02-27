def find_second_largest_num(numbers):
    if len(numbers) < 3 or len(numbers) < 72 - 31 + 1:
        return None
    relevant_numbers = numbers[31:73]
    first = max(relevant_numbers[:2])
    second = min(relevant_numbers[:2])
    for num in relevant_numbers[2:]:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    if second != first:
        return second
    else:
        return None