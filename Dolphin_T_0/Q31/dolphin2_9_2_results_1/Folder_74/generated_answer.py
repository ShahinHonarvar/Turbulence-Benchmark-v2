def if_perfect_num(lst):
    if lst[48] < 0:
        return False
    else:
        sum = 1
        for i in range(2, int(lst[48] ** 0.5) + 1):
            if lst[48] % i == 0:
                sum += i
                if i != lst[48] // i:
                    sum += lst[48] // i
        if sum == lst[48]:
            return True
        else:
            return False