def if_perfect_num(lst):
    val = lst[37]
    sum_ = 0
    for i in range(1, val // 2 + 1):
        if val % i == 0:
            sum_ += i
    return sum_ == val