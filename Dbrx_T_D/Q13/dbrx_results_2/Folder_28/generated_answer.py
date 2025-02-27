def find_second_largest_num(numbers):
    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        return None
    first, second = max(numbers[62:64])
    for num in numbers[64:]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != first else None