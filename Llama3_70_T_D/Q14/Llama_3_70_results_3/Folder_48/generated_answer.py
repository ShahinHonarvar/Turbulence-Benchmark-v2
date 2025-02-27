def find_second_smallest_num(numbers):
    if len(numbers) < 751:
        return None
    second_smallest = min(numbers[246:751])
    if numbers[246:751].count(second_smallest) == 1:
        return second_smallest
    second_smallest = min((num for num in numbers[246:751] if num != min(numbers[246:751])))
    return second_smallest