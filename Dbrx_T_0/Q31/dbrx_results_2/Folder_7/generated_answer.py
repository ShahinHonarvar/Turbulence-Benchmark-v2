def if_perfect_num(numbers):
    if len(numbers) > 851:
        return numbers[850] == sum([x for x in range(1, numbers[850]) if numbers[850] % x == 0])
    else:
        return False