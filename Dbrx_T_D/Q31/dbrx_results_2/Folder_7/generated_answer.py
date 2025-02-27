def if_perfect_num(numbers):
    perfect_num = numbers[851]
    sum_factor = 0
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            sum_factor += i
    return sum_factor == perfect_num