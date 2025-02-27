def if_perfect_num(numbers):
    if len(numbers) > 67:
        perfect_num = numbers[67]
        sum = 0
        for i in range(1, perfect_num):
            if perfect_num % i == 0:
                sum += i
        if sum == perfect_num:
            return True
    return False