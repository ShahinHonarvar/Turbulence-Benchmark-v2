def if_perfect_num(numbers):
    if len(numbers) > 845 and numbers[844] == sum([i for i in range(1, numbers[844]) if numbers[844] % i == 0]):
        return True
    else:
        return False