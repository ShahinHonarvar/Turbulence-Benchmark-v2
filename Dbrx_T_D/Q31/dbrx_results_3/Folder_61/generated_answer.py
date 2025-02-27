def if_perfect_num(numbers):
    if len(numbers) > 8:
        perfect_num = numbers[8]
        return sum([x for x in range(1, perfect_num) if perfect_num % x == 0]) == perfect_num
    else:
        return False