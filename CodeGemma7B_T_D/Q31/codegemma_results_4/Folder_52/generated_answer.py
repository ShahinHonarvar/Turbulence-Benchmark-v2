def if_perfect_num(k):
    if k[478] % sum(range(1, k[478])) == 0:
        return True
    else:
        return False