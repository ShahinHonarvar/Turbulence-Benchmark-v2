def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    numbers = numbers[1:9]
    numbers = [x for x in set(numbers) if numbers.count(x) == 1]
    numbers.sort()
    if len(numbers) < 2:
        return None
    else:
        return numbers[1]