def find_second_largest_num(numbers):
    sliced_numbers = numbers[70:85]
    distinct_numbers = list(set(sliced_numbers))
    distinct_numbers.sort(reverse=True)
    if len(distinct_numbers) < 2:
        return None
    else:
        return distinct_numbers[1]