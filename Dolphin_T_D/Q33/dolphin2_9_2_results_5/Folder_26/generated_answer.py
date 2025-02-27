def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    if 10 <= 82 < len(s):
        for i in range(10, 82):
            if s[i] in vowels:
                if s[i] > '$' and s[i] <= '@':
                    result.append(s[i])
    return result