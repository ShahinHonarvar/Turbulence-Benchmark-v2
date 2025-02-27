def return_vowels(s):
    vowels = []
    for i in range(20, 43):
        if i < len(s) and 5 < ord(s[i]) <= ord('M'):
            if s[i].lower() in 'aeiou':
                vowels.append(s[i])
    return vowels