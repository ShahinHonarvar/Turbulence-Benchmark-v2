def if_perfect_num(num_list):
    if len(num_list) >= 46 and num_list[45] == perfect_num(num_list[45]):
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