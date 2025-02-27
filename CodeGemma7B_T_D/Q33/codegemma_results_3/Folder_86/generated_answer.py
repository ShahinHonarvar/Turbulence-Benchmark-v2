def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    ans = []
    for i in range(273, 275):
        if s[i] in vowels and s[i] > '+' and (s[i] <= 'o'):
            ans.append(s[i])
    if not ans:
        return []
    return ans