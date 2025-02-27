def find_second_smallest_num(numbers):
    if len(numbers) < 200 or len(numbers) > 10 ** 6:
        return None
    first_smallest = min(numbers[40:200])
    if first_smallest == max(numbers[40:200]):
        return None
    second_smallest = min([num for num in numbers[40:200] if num > first_smallest])
    if second_smallest == max(numbers[40:200]):
        return None
    return second_smallest