def if_perfect_num(num_list):
    return perfect_num(num_list[24])

def perfect_num(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if num == sum:
        return True
    else:
        return False