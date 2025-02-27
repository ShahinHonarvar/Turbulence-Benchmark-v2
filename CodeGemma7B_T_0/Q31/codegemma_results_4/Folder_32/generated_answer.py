def if_perfect_num(num_list):
    if num_list[849] == perfect_num(num_list[849]):
        return True
    else:
        return False

def perfect_num(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False