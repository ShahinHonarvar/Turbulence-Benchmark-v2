def find_second_largest_num(numbers):
    if len(numbers) < 201 or numbers[100:201] == []:
        return None
    sublist = sorted(numbers[100:201], reverse=True)
    return sublist[1]