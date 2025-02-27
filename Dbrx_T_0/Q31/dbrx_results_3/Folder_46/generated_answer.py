def if_perfect_num(numbers):
    if len(numbers) > 453 and numbers[453] == sum([i for i in range(1, numbers[453]) if numbers[453] % i == 0]):
        return True
    else:
        return False