def if_perfect_num(numbers):
    if len(numbers) > 100:
        return numbers[100] == sum([x for x in range(1, numbers[100]) if numbers[100] % x == 0])
    else:
        return False