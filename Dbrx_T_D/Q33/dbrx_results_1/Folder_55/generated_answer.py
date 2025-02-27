def return_vowels(s):
    result = []
    for i in range(1, 5):
        if len(s) > i and 'a' <= s[i] <= 'j' and (s[i] in 'aeiou'):
            result.append(s[i])
    return result