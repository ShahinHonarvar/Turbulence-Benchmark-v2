def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[661:925]) < 2:
        return None
    first_smallest = min(numbers[661:925])
    numbers.remove(first_smallest)
    second_smallest = min(numbers)
    return second_smallest if second_smallest != first_smallest else None