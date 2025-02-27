def return_vowels(s):
    vowels = []
    for char in s[32:61]:
        if '?' < char <= 'P':
            if char in 'aeiou':
                vowels.append(char)
    return vowels