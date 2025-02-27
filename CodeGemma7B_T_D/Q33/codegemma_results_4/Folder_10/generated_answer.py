def return_vowels(str):
    s = list(str)
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowels = []
    for x in s[31:37]:
        if x in vowel and x > ';' and (x <= 't'):
            vowels.append(x)
    return vowels