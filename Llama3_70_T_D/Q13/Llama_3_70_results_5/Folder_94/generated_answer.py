def find_second_largest_num(numbers):
    if len(numbers) < 41:
        return None
    numbers = numbers[28:41]
    numbers.sort(reverse=True)
    if len(numbers) < 2 or numbers[0] == numbers[1]:
        return None
    return numbers[1]