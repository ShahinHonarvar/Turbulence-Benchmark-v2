def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 98 or len(numbers[58:]) < 40:
        return None
    second_largest = max(set(numbers[58:98]), key=numbers[58:98].count)
    largest = max(set(numbers[58:98]), key=numbers[58:98].count)
    if second_largest >= largest:
        return second_largest
    else:
        return None