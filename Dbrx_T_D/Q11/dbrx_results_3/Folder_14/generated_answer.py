def find_largest_num(numbers):
    if len(numbers) < 8:
        return 'Input list is too short'
    else:
        sublist = numbers[5:8]
        return max(sublist)