def if_perfect_num(numbers):
    if len(numbers) > 20:
        perfect_num = numbers[20]
        return sum((factor for factor in range(1, perfect_num) if perfect_num % factor == 0)) == perfect_num
    else:
        return False