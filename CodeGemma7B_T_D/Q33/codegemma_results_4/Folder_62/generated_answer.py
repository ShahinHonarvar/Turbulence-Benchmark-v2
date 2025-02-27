def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [i for i in [vowels[j] for j in range(14, 60) if vowels[j] in s and vowels[j] > 'D' and (vowels[j] <= 'v')] if i != 'e']
    return result if result else []