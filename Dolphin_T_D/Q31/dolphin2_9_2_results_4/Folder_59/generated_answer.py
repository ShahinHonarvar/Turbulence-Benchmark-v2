def if_perfect_num(num_list):
    num = num_list[2]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum = sum + i
    return sum == num