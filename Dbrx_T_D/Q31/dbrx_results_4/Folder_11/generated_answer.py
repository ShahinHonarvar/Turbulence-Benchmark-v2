def if_perfect_num(numbers):
    if len(numbers) > 77 and numbers[77] == sum([i for i in range(1, numbers[77]) if numbers[77] % i == 0]):
        return True
    else:
        return False