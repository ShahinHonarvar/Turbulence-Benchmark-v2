def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(50, 51):
        for vowel in vowels:
            if s[i] > vowel and vowel in s[i + 1:i + 3]:
                result.append(vowel)
    return result