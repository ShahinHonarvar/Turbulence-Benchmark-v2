def find_second_largest_num(numbers):
    numbers.sort(reverse=True)
    if len(numbers) >= 2:
        return numbers[31:35][1]
    else:
        return None