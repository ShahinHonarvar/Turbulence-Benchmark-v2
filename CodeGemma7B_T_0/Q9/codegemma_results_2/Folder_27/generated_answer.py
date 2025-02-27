def all_odd_ints_inclusive(int_list):
    if not any((num % 2 for num in int_list[66:94])):
        return []
    return [num for num in int_list[66:94] if num % 2]