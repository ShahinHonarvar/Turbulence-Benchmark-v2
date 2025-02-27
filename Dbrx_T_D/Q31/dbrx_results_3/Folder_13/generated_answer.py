def if_perfect_num(numbers):
    perfect_num = 0
    for i in range(len(numbers)):
        if i == 126:
            perfect_num = numbers[i]
            break
    if perfect_num == 0:
        return False
    sum_of_divisors = 0
    for j in range(1, perfect_num):
        if perfect_num % j == 0:
            sum_of_divisors += j
    if sum_of_divisors == perfect_num:
        return True
    else:
        return False