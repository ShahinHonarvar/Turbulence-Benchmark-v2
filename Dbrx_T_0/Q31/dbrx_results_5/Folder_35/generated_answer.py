def if_perfect_num(numbers):
    if len(numbers) > 993:
        return numbers[992] == sum([x for x in range(1, numbers[992]) if numbers[992] % x == 0])
    else:
        return False