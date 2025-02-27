def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(604, 949) if 'n' < s[i].lower() <= 'u' and s[i].lower() in vowels]
    return result