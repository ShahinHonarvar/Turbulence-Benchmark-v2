def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return 'None'
    otherwise_sorted = sorted(numbers[1:9], reverse=True)
    if len(otherwise_sorted) < 2:
        return 'None'
    else:
        return otherwise_sorted[1]