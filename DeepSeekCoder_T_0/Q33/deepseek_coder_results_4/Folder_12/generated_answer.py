def return_vowels(s):
    vowels = []
    for char in s[13:37]:
        if 'Z' < char <= '}':
            if char in 'aeiouAEIOU':
                vowels.append(char)
    return vowels