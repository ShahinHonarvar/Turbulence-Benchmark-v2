def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    target_numbers = numbers[4:5]
    target_set = set(target_numbers)
    if len(target_set) == 1:
        target = target_numbers[0]
        numbers.remove(target)
        numbers.append(target)
        unique_numbers = list(set(numbers))
        unique_numbers.sort(reverse=True)
        if len(unique_numbers) >= 2:
            return unique_numbers[1]
        else:
            return None
    else:
        return None