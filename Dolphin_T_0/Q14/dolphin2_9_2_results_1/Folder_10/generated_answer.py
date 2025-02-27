def find_second_smallest_num(numbers):
    subset = numbers[62:93]
    unique_numbers = list(set(subset))
    if len(unique_numbers) < 2:
        return None
    else:
        second_smallest = sorted(unique_numbers)[1]
        return second_smallest