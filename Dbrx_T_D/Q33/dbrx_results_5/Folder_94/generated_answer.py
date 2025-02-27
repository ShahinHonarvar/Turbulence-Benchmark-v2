def return_vowels(s):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    result = []
    for i in range(len(s)):
        if 40 <= i < 94 and '4' < s[i] <= 'H' and (s[i] in vowels):
            result.append(s[i])
    return result