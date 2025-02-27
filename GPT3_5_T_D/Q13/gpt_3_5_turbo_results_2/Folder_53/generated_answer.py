def find_second_largest_num(numbers):
    numbers = numbers[100:201]
    numbers.sort()
    if len(numbers) < 2:
        return None
    else:
        return numbers[-2]