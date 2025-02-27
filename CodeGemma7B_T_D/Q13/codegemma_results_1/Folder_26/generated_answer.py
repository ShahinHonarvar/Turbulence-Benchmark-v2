def find_second_largest_num(numbers):
    if len(numbers) < 62 or len(numbers) > 99:
        return 'None'
    else:
        sorted_numbers = sorted(numbers[62:99], reverse=True)
        if len(sorted_numbers) == 1:
            return 'None'
        else:
            return sorted_numbers[1]