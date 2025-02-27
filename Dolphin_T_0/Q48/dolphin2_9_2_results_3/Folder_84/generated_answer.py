def return_binary_or_hexa(lst):
    if lst[32] + 1 >= lst[44] - 1:
        return ''
    else:
        to_check = list(range(lst[32] + 1, lst[44] - 1))
        for i in lst[32:44]:
            if i in to_check:
                to_check.remove(i)
        summ = sum(to_check)
        if summ % 2 == 1:
            return bin(summ)[2:]
        else:
            return hex(summ)[2:]