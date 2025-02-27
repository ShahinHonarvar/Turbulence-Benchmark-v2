def if_perfect_num(numbers):
    if len(numbers) > 94:
        if_perfect = numbers[94] == sum([x for x in range(1, numbers[94]) if numbers[94] % x == 0])
        return if_perfect
    else:
        return False