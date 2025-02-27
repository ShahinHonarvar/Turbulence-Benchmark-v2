def find_second_smallest_num(numbers):
    numbers = numbers[4:5]
    if len(numbers) < 1:
        return None
    else:
        return min(numbers)