def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 73 or (not isinstance(numbers, list)):
        return None
    numbers = numbers[31:73]
    numbers.sort(reverse=True)
    if len(numbers) >= 2 and numbers[0] != numbers[1]:
        return numbers[1]
    else:
        return None