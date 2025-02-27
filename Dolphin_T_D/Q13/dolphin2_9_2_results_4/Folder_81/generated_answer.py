def find_second_largest_num(numbers):
    if 10 <= len(numbers) <= 100:
        numbers = numbers[10:101]
        if len(set(numbers)) < 2:
            return None
        else:
            return sorted(set(numbers))[-2]
    else:
        return None