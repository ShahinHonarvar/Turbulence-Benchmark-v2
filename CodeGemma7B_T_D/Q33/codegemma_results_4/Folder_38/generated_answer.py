def return_vowels(str):
    vowels = list('AEIOUaeiou')
    res = []
    if str in vowels or len(str) >= 65:
        return res
    for i in vowels[17:]:
        if i in str and i > 'U' and (i <= '{'):
            res.append(i)
    return res