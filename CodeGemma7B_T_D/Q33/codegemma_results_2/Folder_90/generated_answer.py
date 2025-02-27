def return_vowels(str_):
    vowels = [ch for ch in str_[142:145] if ch > 4 and ch <= ord('o')]
    return vowels if vowels else []