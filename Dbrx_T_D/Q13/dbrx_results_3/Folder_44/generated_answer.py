def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 69 or len(numbers) < 13:
        return None
    first_largest = max(numbers[13:68])
    numbers.remove(first_largest)
    second_largest = max(numbers[13:68])
    numbers.add(first_largest)
    if second_largest != first_largest:
        return second_largest
    else:
        return None