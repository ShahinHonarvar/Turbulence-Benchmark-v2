def find_second_largest_num(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None
    second_largest_num = None
    for i in range(8, 10):
        if unique_numbers[1] == numbers[i]:
            second_largest_num = numbers[i]
            break
    return second_largest_num