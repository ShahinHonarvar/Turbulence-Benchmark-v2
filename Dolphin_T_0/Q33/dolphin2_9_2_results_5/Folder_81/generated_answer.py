def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(20, 43) if 6 <= ord(s[i]) <= ord('M') and s[i] in vowels]
    return result