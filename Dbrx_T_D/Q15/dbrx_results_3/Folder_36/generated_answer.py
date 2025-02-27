def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 750:
        return 'Error: insufficient number of elements in list'
    elif len(numbers) < 246:
        return 0
    else:
        return sum((numbers[246:751] if i % 2 != 0 else 0 for i in range(246, 751)))