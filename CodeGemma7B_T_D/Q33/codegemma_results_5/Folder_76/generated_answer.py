def return_vowels(a):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = []
    for i in range(495, 837):
        if a[i] in abc[4:] and a[i] > abc[11] and (a[i] <= abc[19]):
            result.append(a[i])
    if len(result) == 0:
        return []
    else:
        return result