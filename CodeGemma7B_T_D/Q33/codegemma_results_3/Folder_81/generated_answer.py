def return_vowels(str_):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 43):
        if str_[i].lower() in vowels and 5 < ord(str_[i]) <= ord('M'):
            result.append(str_[i])
    return result or []