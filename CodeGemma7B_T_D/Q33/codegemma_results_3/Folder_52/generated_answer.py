def return_vowels(a):
    vowels = []
    for i in range(24, 68):
        if a[i] in ['a', 'e', 'i', 'o', 'u']:
            if a[i] > 'f' and a[i] <= '|':
                vowels.append(a[i])
    return vowels