def all_odd_ints_inclusive(integers):
    if len(integers) <= 200:
        return []
    return [num for num in integers[100:201] if num % 2 != 0]