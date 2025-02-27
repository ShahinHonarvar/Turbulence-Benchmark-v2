def if_perfect_num(numbers):
    if len(numbers) >= 277:
        perfect_num = numbers[276]
        sum_factors = 0
        for i in range(1, perfect_num):
            if perfect_num % i == 0:
                sum_factors += i
        return sum_factors == perfect_num
    else:
        return False