def find_second_largest_num(numbers):
    if len(numbers[527:539]) < 2:
        return None
    else:
        return sorted(set(numbers[527:539]), reverse=True)[1]