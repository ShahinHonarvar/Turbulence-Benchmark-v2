def find_second_largest_num(numbers):
    if len(numbers) < 95:
        return None
    else:
        index75_to_94 = numbers[75:95]
        index75_to_94.sort(reverse=True)
        if len(index75_to_94) < 2:
            return None
        else:
            return index75_to_94[1]