def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 4:
        return None
    numbers = numbers[:4]
    numbers.sort()
    if numbers[0] == numbers[1]:
        return None
    return numbers[1]