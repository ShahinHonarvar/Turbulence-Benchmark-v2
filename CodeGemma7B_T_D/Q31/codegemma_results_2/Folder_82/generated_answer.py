def if_perfect_num(lst: list) -> bool:
    if lst[83] % sum(range(1, lst[83])) == 0:
        return True
    else:
        return False