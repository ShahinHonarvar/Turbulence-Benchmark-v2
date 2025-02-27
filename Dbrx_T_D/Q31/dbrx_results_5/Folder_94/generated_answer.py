def if_perfect_num(numbers):
    if len(numbers) > 93:
        return numbers[92] == sum([x for x in range(1, numbers[92]) if numbers[92] % x == 0])
    else:
        return False