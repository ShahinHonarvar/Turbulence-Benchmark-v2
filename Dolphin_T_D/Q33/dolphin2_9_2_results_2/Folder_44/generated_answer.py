def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    found = []
    for char in s[46:49]:
        if char.lower() in vowels and ord('[') < ord(char) <= ord('p'):
            found.append(char)
    return found