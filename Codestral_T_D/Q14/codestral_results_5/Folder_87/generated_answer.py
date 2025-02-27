def find_second_smallest_num(numbers):
    if len(numbers) >= 89 and all((isinstance(num, (int, float)) for num in numbers[22:89])):
        sublist = sorted(numbers[22:89])
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None