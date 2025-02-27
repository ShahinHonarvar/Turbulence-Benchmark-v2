def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 202 <= i < 872 and 3 < s[i] <= '3':
            if s[i] in vowels:
                result.append(s[i])
    return result