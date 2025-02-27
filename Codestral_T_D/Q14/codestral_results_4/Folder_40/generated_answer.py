def find_second_smallest_num(numbers):
    numbers = numbers[:3]
    numbers.sort()
    if len(numbers) < 2:
        return None
    return numbers[1]