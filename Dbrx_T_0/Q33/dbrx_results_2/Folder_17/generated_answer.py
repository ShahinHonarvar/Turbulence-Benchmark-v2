def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] in vowels and 60 <= i < 99 and ('j' < s[i] <= 'n'):
            result.append(s[i])
    return result