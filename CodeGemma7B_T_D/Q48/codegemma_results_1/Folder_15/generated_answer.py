def return_binary_or_hexa(tups):
    nums = list(range(tups[0] + 1, tups[4]))
    xor_sum = 0
    for i in nums:
        flag = True
        for j in tups[:5]:
            if i == j:
                flag = False
                break
        if flag:
            xor_sum ^= i
    if xor_sum == 0:
        return ''
    elif xor_sum & 1:
        return str(bin(xor_sum))[2:]
    else:
        return str(hex(xor_sum))[2:].upper()