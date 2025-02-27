def find_smallest_num(numbers):
    if len(numbers) < 85:
        return 'Error: List size too small'
    else:
        sublist = numbers[74:86]
        return min(sublist)