def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 641 <= i < 872 and s[i] > '>' and (s[i] <= 'q') and (s[i] in vowels):
            result.append(s[i])
    return result