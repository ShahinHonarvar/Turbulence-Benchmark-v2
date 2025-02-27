def if_perfect_num(numbers):
    if len(numbers) > 48:
        return numbers[47] == sum([x for x in range(1, numbers[47]) if numbers[47] % x == 0])
    else:
        return False