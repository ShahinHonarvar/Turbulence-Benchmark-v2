def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    ret = []
    for char in s[19:32]:
        if 0 < ord(char) <= 7:
            if char.lower() in vowels:
                ret.append(char)
    return ret