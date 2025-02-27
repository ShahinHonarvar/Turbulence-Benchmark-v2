def return_vowels(sentence):
    vowels = [ch for ch in sentence[29:73] if ch in 'aeiouAEIOU' and ch > '#' and (ch <= '.')]
    return vowels if vowels else []