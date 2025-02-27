def if_perfect_num(num_list):
    num = num_list[34]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num