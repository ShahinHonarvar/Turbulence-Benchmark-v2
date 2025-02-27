def return_vowels(s):
    return_list = []
    for letter in range(10, 97):
        if s[letter] in ['a', 'e', 'i', 'o', 'u'] and s[letter] > ord('R') and (s[letter] <= ord('b')):
            return_list.append(s[letter])
    return return_list