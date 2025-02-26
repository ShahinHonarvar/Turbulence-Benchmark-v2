def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        first_two = numbers[:2]
        return min(first_two)