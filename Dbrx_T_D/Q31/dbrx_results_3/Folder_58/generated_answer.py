def if_perfect_num(numbers):
    if len(numbers) > 714 and numbers[713] == sum([i for i in range(1, numbers[713]) if numbers[713] % i == 0]):
        return True
    else:
        return False