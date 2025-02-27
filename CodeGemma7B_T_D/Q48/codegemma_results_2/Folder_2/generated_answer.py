def return_binary_or_hexa(tpl):
    target = [x for x in range(tpl[72] + 1, tpl[93])]
    if not all((x in tpl for x in target)):
        return bin(sum(set(target) - set(tpl[72:94])))[2:]
    else:
        return hex(sum(set(target) - set(tpl[72:94])))[2:].upper()