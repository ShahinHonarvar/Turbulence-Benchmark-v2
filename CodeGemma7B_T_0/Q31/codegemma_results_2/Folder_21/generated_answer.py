def if_perfect_num(num_list):
    if num_list[410] == perfect_num(num_list[410]):
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