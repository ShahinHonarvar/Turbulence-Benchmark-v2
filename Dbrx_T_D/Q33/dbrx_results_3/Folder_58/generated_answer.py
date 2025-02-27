def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(260, 322) if s[i] > '%' and s[i] <= 'U' and (s[i] in vowels)]