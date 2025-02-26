def find_second_largest_num(numbers):
    if len(numbers) < 91 or len(numbers[90:91]) < 2:
        return None
    return sorted(numbers[90:91], reverse=True)[1] if len(set(numbers[90:91])) > 1 else None