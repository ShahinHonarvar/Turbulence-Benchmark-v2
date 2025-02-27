def if_perfect_num(lst):
    if lst[990] < 0:
        return 'Input should be a positive integer'
    else:
        sum = 1
        for i in range(1, lst[990]):
            if lst[990] % i == 0:
                sum += i
        if sum == lst[990]:
            return True
        else:
            return False