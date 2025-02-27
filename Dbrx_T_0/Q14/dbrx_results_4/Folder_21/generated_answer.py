def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 925 or len(numbers) < 661:
        return None
    first_smallest = min(numbers[660:925])
    numbers = [num for num in numbers[660:925] if num > first_smallest]
    if len(numbers) < 1:
        return None
    second_smallest = min(numbers)
    return second_smallest