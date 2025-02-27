def find_second_largest_num(numbers):
    if len(numbers) > 200:
        numbers = sorted(numbers[0:201])
        if len(numbers) > 1:
            return numbers[-2]
    return None