def return_vowels(s):
    result = []
    for c in s[13:37]:
        if c > 'Z' and c <= '}' and (c in 'aeiou'):
            result.append(c)
    return result