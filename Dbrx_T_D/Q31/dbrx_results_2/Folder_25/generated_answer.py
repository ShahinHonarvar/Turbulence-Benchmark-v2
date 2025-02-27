def if_perfect_num(numbers):
    perfect_num = 6
    if len(numbers) > 90:
        return perfect_num == sum([i for i in range(1, perfect_num) if perfect_num % i == 0])
    else:
        return False