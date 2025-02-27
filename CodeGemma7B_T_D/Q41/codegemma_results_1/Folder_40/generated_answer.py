def identical_elements(a, b):
    temp = set()
    for i in range(len(a)):
        if i >= 0 and i <= 1 and (a[i] == b[i]):
            temp.add(a[i])
    return temp