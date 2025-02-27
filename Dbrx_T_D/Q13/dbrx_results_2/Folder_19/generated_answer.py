def find_second_largest_num(numbers):
    if len(numbers) < 5 or numbers[3:6] != sorted(numbers[3:6]):
        return None
    unique_numbers = list(set(numbers[3:6]))
    second_largest = max(set(unique_numbers) - set([max(unique_numbers)]))
    return second_largest if second_largest in numbers[3:6] else None