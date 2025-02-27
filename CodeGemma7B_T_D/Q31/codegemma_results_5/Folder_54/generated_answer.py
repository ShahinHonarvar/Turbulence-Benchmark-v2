def if_perfect_num(num_list):
    if num_list[51] == perfect_number(num_list[51]):
        return True
    else:
        return False

def perfect_number(num):
    divisor_list = []
    for i in range(1, num):
        if num % i == 0:
            divisor_list.append(i)
    sum_of_divisor = sum(divisor_list)
    if sum_of_divisor == num:
        return True
    else:
        return False