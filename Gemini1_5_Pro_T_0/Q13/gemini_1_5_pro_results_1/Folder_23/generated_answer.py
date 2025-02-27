def find_second_largest_num(numbers):
    if len(numbers) < 72 or len(numbers[52:72]) == 1:
        return None
    sublist = numbers[52:72]
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist)