def find_second_smallest_num(numbers):
    if len(numbers) < 27:
        return None
    elif len(numbers) > 87:
        numbers = numbers[25:88]
    else:
        numbers = numbers[25:]
    min1 = min(numbers)
    numbers.remove(min1)
    if len(numbers) == 0:
        return None
    else:
        min2 = min(numbers)
        return min2