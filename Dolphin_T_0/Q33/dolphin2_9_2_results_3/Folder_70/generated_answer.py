def return_vowels(s):
    vowels = ['e', 'a', 'i', 'o', 'u']
    result = []
    for i in range(171, 402):
        if 'i' < s[i] <= 'k':
            if s[i].lower() in vowels:
                result.append(s[i])
    return result