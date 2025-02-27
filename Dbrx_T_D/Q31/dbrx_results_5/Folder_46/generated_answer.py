def if_perfect_num(numbers):
    return True if numbers[453] == sum([i for i in range(1, numbers[453]) if numbers[453] % i == 0]) else False