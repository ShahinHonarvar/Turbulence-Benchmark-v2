def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[35:50]
    numbers.sort(reverse=True)
    if numbers[0] == numbers[1]:
        return None
    return numbers[1]