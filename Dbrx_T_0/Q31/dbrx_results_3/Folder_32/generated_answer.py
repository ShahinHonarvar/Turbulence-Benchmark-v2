def if_perfect_num(numbers):
    if len(numbers) > 849 and numbers[849] == sum([i for i in range(1, numbers[849]) if numbers[849] % i == 0]):
        return True
    else:
        return False