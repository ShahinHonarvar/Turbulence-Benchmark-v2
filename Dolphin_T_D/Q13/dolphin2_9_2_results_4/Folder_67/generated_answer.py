def find_second_largest_num(numbers):
    if 22 <= len(numbers) <= 50:
        numbers = numbers[22:51]
        numbers.sort()
        if len(numbers) > 1:
            return numbers[-2]
    return None