def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_largest = max(numbers[59:98])
    numbers.remove(first_largest)
    second_largest = max(numbers[59:98])
    return second_largest if second_largest < first_largest else None