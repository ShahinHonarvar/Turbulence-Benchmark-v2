def return_vowels(s):
    vowels = ['b', 'c', 'd', 'e', 'f', 'g']
    result = []
    for i in range(464, 574):
        if s[i] in vowels:
            result.append(s[i])
    return result