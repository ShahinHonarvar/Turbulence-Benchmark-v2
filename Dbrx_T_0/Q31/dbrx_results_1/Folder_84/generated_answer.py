def if_perfect_num(numbers):
    if len(numbers) > 685 and numbers[685] == sum([i for i in range(1, numbers[685]) if numbers[685] % i == 0]):
        return True
    else:
        return False