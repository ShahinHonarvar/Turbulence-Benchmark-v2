def if_perfect_num(lst):
    if len(lst) > 96:
        num = lst[96]
        return sum((i for i in range(1, num) if num % i == 0)) == num
    return False