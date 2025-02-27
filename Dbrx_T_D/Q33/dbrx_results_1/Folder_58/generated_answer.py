def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(260, 322) if s[i] > '%' and s[i] <= 'U' and (s[i] in vowels)]
    return result