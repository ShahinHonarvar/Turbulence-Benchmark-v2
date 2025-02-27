def return_vowels(str1):
    vowels = []
    for ch in str1[60:99]:
        if ch >= 'j' and ch <= 'n' and (ch in 'aeiouAEIOU'):
            vowels.append(ch)
    return vowels