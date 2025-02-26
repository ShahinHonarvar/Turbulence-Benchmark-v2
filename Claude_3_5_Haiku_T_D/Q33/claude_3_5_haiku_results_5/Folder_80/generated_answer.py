def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(85, 99):
        if index < len(s):
            char = s[index].lower()
            if char in vowels and '/' < char <= 'n':
                result.append(char)
    return result