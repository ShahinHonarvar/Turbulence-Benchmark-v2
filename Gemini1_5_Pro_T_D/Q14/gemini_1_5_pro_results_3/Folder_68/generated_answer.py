def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    else:
        distinct_numbers = set(numbers[:9])
        if len(distinct_numbers) < 2:
            return None
        else:
            sorted_numbers = sorted(distinct_numbers)
            return sorted_numbers[1]