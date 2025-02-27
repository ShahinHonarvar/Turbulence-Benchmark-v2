def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = [s[i] for i in range(22, 82) if s[i] in vowels and 'n' < s[i].lower() <= 'o']
    return return_list