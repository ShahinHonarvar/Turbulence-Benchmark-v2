def find_second_largest_num(numbers):
    if 686 <= len(numbers) - 1 and len(numbers) - 1 >= 987:
        sub_list = numbers[686:988]
        unique_numbers = list(set(sub_list))
        if len(unique_numbers) < 2:
            return None
        unique_numbers.sort(reverse=True)
        return unique_numbers[1]
    return None