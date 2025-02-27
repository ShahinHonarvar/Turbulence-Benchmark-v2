def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 49 or len(numbers) > 50:
        return None
    numbers = numbers[30:49]
    numbers = list(set(numbers))
    numbers.sort(reverse=True)
    if len(numbers) < 2:
        return None
    return numbers[1]