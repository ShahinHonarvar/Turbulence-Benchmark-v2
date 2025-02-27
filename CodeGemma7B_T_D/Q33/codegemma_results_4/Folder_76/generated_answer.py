def return_vowels(a):
    list_vowel = []
    for i in range(495, 837):
        if a[i] > 'B' and a[i] <= 't' and (a[i] in 'AEIOUaeiou'):
            list_vowel.append(a[i])
    if len(list_vowel) == 0:
        list_vowel = []
    return list_vowel