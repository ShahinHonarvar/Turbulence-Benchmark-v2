def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 88 - 75 + 1:
        return None
    first_part = numbers[75:89]
    distinct_first_part = list(set(first_part))
    distinct_first_part.sort(reverse=True)
    if len(distinct_first_part) < 2:
        return None
    return distinct_first_part[1]