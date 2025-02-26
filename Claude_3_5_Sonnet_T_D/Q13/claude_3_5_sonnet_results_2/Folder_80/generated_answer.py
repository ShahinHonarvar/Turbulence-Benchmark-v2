def find_second_largest_num(numbers):
    if len(numbers) < 67 or len(set(numbers[64:67])) < 2:
        return None
    return sorted(numbers[64:67], reverse=True)[1]