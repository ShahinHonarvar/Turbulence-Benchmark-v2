def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 7:
        return None
    smallest = min(numbers[0:7])
    second_smallest = None
    for num in numbers[0:7]:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest