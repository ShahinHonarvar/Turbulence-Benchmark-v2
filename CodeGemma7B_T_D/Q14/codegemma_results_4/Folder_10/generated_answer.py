def find_second_smallest_num(numbers):
    numbers = sorted(numbers)
    if len(numbers) < 63 or numbers[62] == numbers[-1]:
        return None
    return sorted(numbers[62:93])[1]