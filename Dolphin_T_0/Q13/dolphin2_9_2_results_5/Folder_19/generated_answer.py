def find_second_largest_num(numbers):
    if len(numbers) == 0 or len(set(numbers[3:6])) == 1:
        return None
    else:
        numbers = numbers[3:6]
        first = max(numbers)
        numbers.remove(first)
        second = max(numbers)
        return second