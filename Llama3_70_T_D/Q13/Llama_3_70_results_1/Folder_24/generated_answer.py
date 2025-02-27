def find_second_largest_num(numbers):
    if len(numbers) < 96:
        return None
    numbers = numbers[74:96]
    numbers = list(set(numbers))
    numbers.sort(reverse=True)
    if len(numbers) < 2:
        return None
    return numbers[1]