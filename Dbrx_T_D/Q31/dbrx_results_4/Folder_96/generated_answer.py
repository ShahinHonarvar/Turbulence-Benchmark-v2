def if_perfect_num(numbers):
    if len(numbers) > 47 and numbers[47] == sum([x for x in range(1, numbers[47]) if numbers[47] % x == 0]):
        return True
    else:
        return False