def find_second_largest_num(numbers):
    if not numbers[75:89]:
        return None
    distinct_numbers = list(set(numbers[75:89]))
    distinct_numbers.sort(reverse=True)
    if len(distinct_numbers) < 2:
        return None
    return distinct_numbers[1]