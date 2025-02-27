def if_perfect_num(int_list):
    if len(int_list) > 87:
        num = int_list[87]
        return num > 0 and sum((i for i in range(1, num) if num % i == 0)) == num
    else:
        return False