def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        six_to_six = numbers[6:7]
        if len(set(six_to_six)) < 2:
            return None
        else:
            return sorted(set(six_to_six))[1]