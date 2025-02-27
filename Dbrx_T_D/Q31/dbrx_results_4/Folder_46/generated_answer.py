def if_perfect_num(numbers):
    if len(numbers) > 453 and numbers[453] > 0:
        perfect_num = sum([i for i in range(1, numbers[453]) if numbers[453] % i == 0])
        return perfect_num == numbers[453]
    else:
        return False