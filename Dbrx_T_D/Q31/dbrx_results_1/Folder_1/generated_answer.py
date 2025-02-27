def if_perfect_num(numbers):
    if len(numbers) > 85:
        return numbers[84] == sum([x for x in range(1, numbers[84]) if numbers[84] % x == 0])
    else:
        return False