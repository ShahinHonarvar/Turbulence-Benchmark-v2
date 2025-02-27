def find_second_largest_num(numbers):
    specified_range = numbers[62:79]
    distinct_numbers = set(specified_range)
    if len(distinct_numbers) < 2:
        return None
    return sorted(distinct_numbers)[-2]