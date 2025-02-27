def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 538 or 527 > len(numbers) - 1:
        return None
    first_part = numbers[527:len(numbers) - 1]
    second_part = numbers[len(numbers) - 538:]
    combined = first_part + second_part
    combined.sort(reverse=True)
    if combined[0] == combined[1]:
        return combined[1]
    else:
        return combined[0]