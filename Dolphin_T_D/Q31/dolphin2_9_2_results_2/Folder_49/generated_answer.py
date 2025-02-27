def if_perfect_num(lst):
    if lst[68] > 0:
        sum_ = 1
        for i in range(2, lst[68] // 2 + 1):
            if lst[68] % i == 0:
                sum_ += i
        if sum_ == lst[68]:
            return True
    return False