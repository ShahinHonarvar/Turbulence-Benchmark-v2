def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 30 or len(numbers) < 200:
        return None
    first_smallest = min(numbers[30:200])
    second_smallest = None
    for num in numbers[30:200]:
        if num > first_smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest if second_smallest != first_smallest else None