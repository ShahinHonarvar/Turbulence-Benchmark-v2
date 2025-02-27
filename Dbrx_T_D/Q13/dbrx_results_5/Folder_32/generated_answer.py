def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 98:
        return None
    numbers = numbers[21:98]
    numbers.sort(reverse=True)
    if numbers[0] != numbers[1]:
        return numbers[1]
    else:
        return None