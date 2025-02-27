def all_odd_ints_exclusive(num_list):
    if not any((number % 2 for number in num_list[0:5])):
        return []
    return [number for number in num_list[0:5] if number % 2]