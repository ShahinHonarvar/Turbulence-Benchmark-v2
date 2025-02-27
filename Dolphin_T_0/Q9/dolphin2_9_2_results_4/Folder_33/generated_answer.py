def all_odd_ints_inclusive(numbers):
    result = [num for num in numbers[667:775:2]]
    if result:
        return result
    else:
        return []