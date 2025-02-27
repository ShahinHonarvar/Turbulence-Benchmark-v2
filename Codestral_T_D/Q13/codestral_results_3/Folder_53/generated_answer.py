def find_second_largest_num(numbers):
    if len(numbers) >= 201:
        sublist = numbers[100:201]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[-2]
    return None