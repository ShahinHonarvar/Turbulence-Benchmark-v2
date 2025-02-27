def return_binary_or_hexa(test_tup):
    test_tup = sorted(test_tup)
    last = test_tup[933] + 1
    curr = test_tup[933] + 1
    res = 0
    while curr <= test_tup[996]:
        if curr not in test_tup:
            res += curr
        curr += 1
    if res % 2 == 1:
        return f'{res:b}'
    else:
        return f'{res:x}'