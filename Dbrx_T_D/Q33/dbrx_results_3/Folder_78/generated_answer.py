def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= '@' and s[i] <= '[' and (45 < i < 90):
            if s[i].lower() in vowels:
                result.append(s[i])
    return result