def if_perfect_num(num_list):
    if len(num_list) < 1:
        return False
    sum = 0
    for i in range(1, num_list[0]):
        if num_list[0] % i == 0:
            sum += i
    return sum == num_list[0]