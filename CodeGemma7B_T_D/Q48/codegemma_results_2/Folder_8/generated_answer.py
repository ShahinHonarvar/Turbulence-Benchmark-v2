def return_binary_or_hexa(x):
    sig_b = '0b'
    sig_h = '0x'
    arr = [i for i in range(max(x)) if i not in x]
    summ = sum(arr)
    if summ % 2 == 0:
        if len(str(summ)) % 2 == 0:
            for i in reversed(str(summ)):
                sig_h = sig_h + i.upper()
        else:
            for i in reversed(str(summ)):
                sig_h = sig_h + i.upper()
        return sig_h
    else:
        if len(str(summ)) % 2 == 0:
            for i in reversed(bin(summ)[2:]):
                sig_b = sig_b + i
        else:
            for i in reversed(bin(summ)[2:]):
                sig_b = sig_b + i
        return sig_b