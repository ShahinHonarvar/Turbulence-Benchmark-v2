def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return 'None'
    smallest = min(numbers)
    numbers.remove(smallest)
    if len(numbers) == 0:
        return 'None'
    second_smallest = min(numbers)
    return second_smallest