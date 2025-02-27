def if_perfect_num(numbers):
    if len(numbers) > 37:
        perfect_num = numbers[37]
        return perfect_num == sum([i for i in range(1, perfect_num) if perfect_num % i == 0])
    else:
        return False