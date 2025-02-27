def if_perfect_num(lst):
    if lst[685] == sum([i for i in range(1, lst[685]) if lst[685] % i == 0]):
        return True
    else:
        return False