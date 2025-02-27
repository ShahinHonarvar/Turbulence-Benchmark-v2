def if_perfect_num(numbers):
    if len(numbers) > 321 and numbers[321] == sum([i for i in range(1, numbers[321]) if numbers[321] % i == 0]):
        return True
    else:
        return False