def return_binary_or_hexa(tup):
    tot = 0
    for num in range(tup[56] + 1, tup[90]):
        if num not in tup[56:90]:
            tot += num
    return int2string(tot, 2) if tot % 2 else int2string(tot, 16)

def int2string(i, base):
    if i == 0:
        return '0'
    nums = []
    while i:
        i, r = divmod(i, base)
        nums.append(str(r))
    return ''.join(nums[::-1])