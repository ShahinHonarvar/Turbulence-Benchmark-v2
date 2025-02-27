def all_odd_ints_exclusive(numbers):
    if not any((i % 2 for i in numbers[14:100])):
        return []
    return [i for i in numbers[14:100] if i % 2]