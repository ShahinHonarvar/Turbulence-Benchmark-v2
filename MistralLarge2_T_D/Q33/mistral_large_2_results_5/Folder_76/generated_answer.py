def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [s[i] for i in range(495, 837) if s[i] in vowels and 'B' < s[i] <= 't']