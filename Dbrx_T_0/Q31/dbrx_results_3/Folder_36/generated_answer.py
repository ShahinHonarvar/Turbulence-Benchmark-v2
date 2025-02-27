def if_perfect_num(numbers):
    if len(numbers) > 990 and numbers[990] == sum([i for i in range(1, numbers[990]) if numbers[990] % i == 0]):
        return True
    else:
        return False