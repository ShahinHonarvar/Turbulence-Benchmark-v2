def return_binary_or_hexa(t):
    a, b = (t[86], t[99])
    sum_ = [i for i in range(a + 1, b) if i not in t[86:99]]
    if sum_ == []:
        return ''
    sum_in_int = sum(sum_)
    return bin(sum_in_int)[2:].zfill(4) if sum_in_int % 2 else hex(sum_in_int)[2:].zfill(2)