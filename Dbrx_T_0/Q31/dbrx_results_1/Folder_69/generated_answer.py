def if_perfect_num(numbers):
    if len(numbers) > 459 and numbers[458] == sum([i for i in range(1, numbers[458]) if numbers[458] % i == 0]):
        return True
    else:
        return False