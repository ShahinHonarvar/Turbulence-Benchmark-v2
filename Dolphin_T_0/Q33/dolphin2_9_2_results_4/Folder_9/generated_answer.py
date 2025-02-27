def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(13, 35) if 8 < ord(s[i]) <= ord('F') and s[i].lower() in vowels]
    return result