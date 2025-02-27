def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    else:
        sublist = numbers[35:50]
        unique_nums = sorted(set(sublist))
        if len(unique_nums) < 2:
            return None
        else:
            return unique_nums[-2]