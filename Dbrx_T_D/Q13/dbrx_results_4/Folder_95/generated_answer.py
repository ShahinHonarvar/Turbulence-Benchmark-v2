def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 1000:
        return None
    sorted_numbers = sorted(numbers[82:87], reverse=True)
    if len(sorted_numbers) < 2:
        return None
    second_largest = sorted_numbers[1]
    return second_largest if second_largest != sorted_numbers[0] else None