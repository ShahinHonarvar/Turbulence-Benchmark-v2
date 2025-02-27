def return_binary_or_hexa(t):
    a, b = (t[0], t[8])
    total = sum((i for i in range(a + 1, b) if i not in t))
    if total % 2:
        if total < 0:
            return '{0:b}'.format(total & 4294967295)[1:]
        else:
            return '{0:b}'.format(total)[1:]
    elif total < 0:
        return '{0:x}'.format(total & 4294967295)
    else:
        return '{0:x}'.format(total)
    return ''