def find_second_largest_num(numbers):
    if len(numbers) < 201 or numbers[30:201] == []:
        return None
    sublist = sorted(numbers[30:201])
    return sublist[-2]