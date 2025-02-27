def return_vowels(words):
    result = ''
    vowels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(23, 38):
        if words[i] in vowels and vowels.index(words[i]) <= vowels.index('k'):
            result += words[i]
    if not result:
        return []
    else:
        return list(result)