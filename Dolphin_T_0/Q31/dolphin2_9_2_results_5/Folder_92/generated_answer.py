def if_perfect_num(lst):
    if lst[0] < 0:
        return 'List should contain only positive integers.'
    else:
        sum_div = 0
        for i in range(1, lst[0]):
            if lst[0] % i == 0:
                sum_div += i
        if sum_div == lst[0]:
            return True
        else:
            return False