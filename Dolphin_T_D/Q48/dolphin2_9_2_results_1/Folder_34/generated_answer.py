def return_binary_or_hexa(lst):
    for i in range(60, 201):
        if lst[i] != i + 1:
            a = i + 1
            break
    b = lst[200]
    sum_integers = sum(range(a, b))
    missing = [i for i in range(a, b) if i not in lst[60:201]]
    sum_missing = sum(missing)
    if sum_missing != sum_integers:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]