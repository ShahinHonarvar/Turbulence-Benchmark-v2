def if_perfect_num(numbers):
    if len(numbers) > 95:
        perfect_num = numbers[94]
        return perfect_num > 0 and sum((i for i in range(1, perfect_num) if perfect_num % i == 0)) == perfect_num
    else:
        return False