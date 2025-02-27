def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 85:
        return None
    second_largest = None
    largest = max(numbers[70:85])
    for num in numbers[70:85]:
        if num < largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest