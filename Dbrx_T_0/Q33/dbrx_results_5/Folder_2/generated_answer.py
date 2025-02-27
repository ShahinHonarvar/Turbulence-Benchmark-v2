def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 170 <= i < 645 and s[i] > 'E' and (s[i] <= '~') and (s[i] in vowels):
            result.append(s[i])
    return result