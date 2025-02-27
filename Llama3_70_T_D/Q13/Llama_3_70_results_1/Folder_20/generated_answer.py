def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    else:
        subset = sorted(numbers[56:67], reverse=True)
        if len(set(subset)) < 2:
            return None
        else:
            return subset[1]