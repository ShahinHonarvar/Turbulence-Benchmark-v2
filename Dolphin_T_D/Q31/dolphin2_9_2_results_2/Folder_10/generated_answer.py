def if_perfect_num(lst):
    perfect_num = lst[54]
    if perfect_num < 1:
        return False
    else:
        sum = 1
        for i in range(2, int(perfect_num / 2) + 1):
            if perfect_num % i == 0:
                sum += i
        return sum == perfect_num