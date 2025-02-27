def all_even_ints_inclusive(a):
    result = []
    for i in range(56, 58):
        if i in range(len(a)):
            if a[i] % 2 == 0:
                result.append(a[i])
    return result