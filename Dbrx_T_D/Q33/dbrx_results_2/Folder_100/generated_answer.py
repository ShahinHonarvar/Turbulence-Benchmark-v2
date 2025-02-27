def return_vowels(s):
    result = []
    for i in range(23, 75):
        if s[i] > 'L' and s[i] <= 'd' and (s[i] in 'AEIOUaeiou'):
            result.append(s[i])
    return result