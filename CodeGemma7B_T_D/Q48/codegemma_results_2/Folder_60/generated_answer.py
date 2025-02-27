def return_binary_or_hexa(a, b, tup):
    idx = 0
    btoi = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    cark = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    arr = []
    sum2 = 0
    for i in range(a + 1, b):
        if tup[idx] == i:
            idx += 1
        else:
            arr.append(i)
            sum2 += i
    if not arr:
        return ''
    elif sum2 % 2:
        arr.sort(reverse=True)
        temp = ''
        for i in arr:
            temp += btoi[i % 2]
            i //= 2
        return temp
    else:
        sum2 = 0
        for i in arr:
            sum2 += cark[i]
        return str(hex(sum2))[2:]