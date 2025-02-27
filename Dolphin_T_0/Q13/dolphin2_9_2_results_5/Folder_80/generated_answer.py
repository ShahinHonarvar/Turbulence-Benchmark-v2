def find_second_largest_num(numbers):
    if numbers[64:67]:
        return sorted(numbers[64:67])[-2]
    else:
        return None