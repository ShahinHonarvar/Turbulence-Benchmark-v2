def return_vowels(s):
    vowels = []
    for char in s[47:61]:
        if char > chr(9) and char <= chr(79):
            if char in 'aeiouAEIOU':
                vowels.append(char)
    return vowels