def find_second_smallest_num(numbers):
    numbers = numbers[0:10]
    if len(numbers) < 2:
        return None
    smallest = min(numbers)
    numbers.remove(smallest)
    second_smallest = min(numbers)
    return second_smallest