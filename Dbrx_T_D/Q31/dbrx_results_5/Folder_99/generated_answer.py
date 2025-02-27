def if_perfect_num(numbers):
    if len(numbers) > 733 and numbers[733] == sum([i for i in range(1, numbers[733]) if numbers[733] % i == 0]):
        return True
    else:
        return False