def if_perfect_num(lst):
    if sum([i for i in range(1, lst[453]) if not lst[453] % i]) == lst[453]:
        return True
    else:
        return False