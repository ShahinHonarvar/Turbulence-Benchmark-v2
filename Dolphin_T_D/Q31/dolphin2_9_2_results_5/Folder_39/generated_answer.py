def if_perfect_num(numbers):
    if len(numbers) >= 60:
        perfect_num = numbers[59]
        sum_div = 0
        for i in range(1, perfect_num):
            if perfect_num % i == 0:
                sum_div += i
        if sum_div == perfect_num:
            return True
        else:
            return False
    else:
        return False