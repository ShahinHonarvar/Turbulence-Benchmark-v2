def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(770, 852) if s[i] in vowels and 'b' < s[i] <= 'i']
    return result