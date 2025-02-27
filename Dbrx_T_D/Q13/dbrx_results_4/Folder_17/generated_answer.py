def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 62 or len(numbers) < 78:
        return None
    min_num = min(numbers[:79])
    second_largest = max(filter(lambda x: x > min_num, numbers[62:79]))
    return second_largest if second_largest != max(numbers[62:79]) else None