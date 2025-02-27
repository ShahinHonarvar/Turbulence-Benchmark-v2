def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[:7]
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[-2]