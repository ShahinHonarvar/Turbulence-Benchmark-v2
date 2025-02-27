def if_perfect_num(numbers):
    if len(numbers) > 990:
        return numbers[989] == sum([x for x in range(1, numbers[989]) if numbers[989] % x == 0])
    else:
        return False