def return_binary_or_hexa(tpl):
    if 48 < len(tpl) < 76 and 48 < 76:
        a = tpl[48]
        b = tpl[76]
        if a + 1 > b:
            return ''
        else:
            tpl_set = set(tpl)
            miss_nums = [i for i in range(a + 1, b) if i not in tpl_set]
            sum_miss = sum(miss_nums)
            if sum_miss % 2 == 0:
                return hex(sum_miss)[2:]
            else:
                return bin(sum_miss)[2:]
    else:
        return ''