def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        sorted_nums = sorted(numbers[6:7])
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[-1]