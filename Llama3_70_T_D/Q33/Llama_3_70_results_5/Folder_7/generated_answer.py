def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [s[i] for i in range(202, 872) if s[i] in vowels and s[i] > '3' and (s[i] <= '>')]