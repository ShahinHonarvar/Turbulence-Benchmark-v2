def if_perfect_num(a):
    for i in a:
        if i == a[99]:
            if sum([i for i in range(1, a[100]) if a[100] % i == 0]) == a[100]:
                return True
    return False