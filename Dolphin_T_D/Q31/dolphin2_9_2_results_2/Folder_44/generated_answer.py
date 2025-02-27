def if_perfect_num(lst):
    perfect_num = lst[828]
    sum_ = sum([i for i in range(1, perfect_num) if perfect_num % i == 0])
    return sum_ + 1 == perfect_num