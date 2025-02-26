def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(60, 99):
        if i < len(s):
            char = s[i].lower()
            if char in vowels and 'j' < char <= 'n':
                result.append(s[i])
    return result