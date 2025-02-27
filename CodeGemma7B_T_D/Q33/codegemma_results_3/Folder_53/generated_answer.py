def return_vowels(txt):
    Vowels = []
    for i in txt[27:57]:
        if i in 'aeiouAEIOU':
            if i > 'o' and i <= 'w':
                Vowels.append(i)
    if not Vowels:
        return []
    return Vowels