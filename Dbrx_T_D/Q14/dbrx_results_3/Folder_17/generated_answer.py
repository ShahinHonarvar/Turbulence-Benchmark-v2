def find_second_smallest_num(numbers):
    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        return None
    first_smallest = min(numbers[28:39])
    first_smallest_index = numbers[28:39].index(first_smallest) + 28
    if first_smallest_index + 1 > 38 or numbers[first_smallest_index + 1] == first_smallest:
        return None
    numbers = numbers[:]
    del numbers[first_smallest_index]
    second_smallest = min(numbers[28:39])
    return second_smallest