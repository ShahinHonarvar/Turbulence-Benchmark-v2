def return_vowels(s):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    ans, result = ([], [])
    for i in range(len(s)):
        if s[i] in vowels_list:
            ans.append(s[i])
    for i in range(29, 31):
        if ans[i] > 'a' and ans[i] <= 'f':
            result.append(ans[i])
    return result