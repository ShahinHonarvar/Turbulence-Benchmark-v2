def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 10:
        return None
    unique_numbers = set(numbers[:11])
    if len(unique_numbers) < 2:
        return None
    largest_num = max(unique_numbers)
    unique_numbers.remove(largest_num)
    return max(unique_numbers)