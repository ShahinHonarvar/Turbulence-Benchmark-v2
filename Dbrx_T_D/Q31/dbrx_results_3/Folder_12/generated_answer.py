def if_perfect_num(numbers):
    if len(numbers) >= 27:
        return numbers[26] == sum([x for x in range(1, numbers[26]) if numbers[26] % x == 0])
    else:
        return False