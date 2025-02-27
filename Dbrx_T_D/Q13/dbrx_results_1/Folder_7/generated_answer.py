def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 924 - 661 + 1:
        return None
    first_part = numbers[661:925]
    sorted_part = sorted(first_part)
    if sorted_part[-2] == sorted_part[-1]:
        return None
    return sorted_part[-2]