def return_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_int = []
    for i in range(14, 60):
        if s[i] in vowels and ord(s[i]) > ord('D') and (ord(s[i]) <= ord('v')):
            vowels_int.append(s[i])
    return vowels_int