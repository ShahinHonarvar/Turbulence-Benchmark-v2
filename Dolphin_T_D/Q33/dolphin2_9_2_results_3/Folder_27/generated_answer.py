def return_vowels(s):
    vowels = []
    for ch in s[29:31]:
        if 'a' < ch <= 'f' and ch in 'aeiou':
            vowels.append(ch)
    return vowels