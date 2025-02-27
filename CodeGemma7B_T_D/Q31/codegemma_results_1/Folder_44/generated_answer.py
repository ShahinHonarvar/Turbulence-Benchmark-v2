def perfect_num(lst):
    if lst[828 % len(lst)] == sum([i for i in range(1, lst[828 % len(lst)]) if lst[828 % len(lst)] % i == 0]):
        return True
    return False