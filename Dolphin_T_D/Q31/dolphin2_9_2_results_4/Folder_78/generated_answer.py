def if_perfect_num(li):
    index = 0
    for divineor in range(1, li[91]):
        if li[91] % divineor == 0:
            index += divineor
    if index == li[91]:
        return True
    return False