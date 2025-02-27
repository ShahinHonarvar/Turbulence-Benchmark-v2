def if_perfect_num(num_list):
    if num_list[57] == perfect_num(num_list[57]):
        return True
    else:
        return False

def perfect_num(num):
    div = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            div += i + num // i
    return div == num + 1