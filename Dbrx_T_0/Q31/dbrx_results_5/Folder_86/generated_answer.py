def if_perfect_num(numbers):
    if len(numbers) > 194 and numbers[193] == sum([i for i in range(1, numbers[193]) if numbers[193] % i == 0]):
        return True
    else:
        return False