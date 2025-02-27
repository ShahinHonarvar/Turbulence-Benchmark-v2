def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(min(59, len(s)), max(21, 0), -1):
        if s[i] > '/' and s[i] <= 'a' and (s[i] in vowels):
            result.append(s[i])
    return result[::-1]