def if_perfect_num(num_list):
    if not num_list or num_list[83] <= 0:
        return False
    sum = 1
    for i in range(2, num_list[83]):
        if num_list[83] % i == 0:
            sum += i
    return sum == num_list[83]