def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 100:
        return None
    else:
        numbers = numbers[1:101]
        numbers.sort()
        return numbers[1]