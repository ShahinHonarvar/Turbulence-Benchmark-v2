def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[90:97]:
        if vowels.count(char.lower()) > 0:
            result.append(char)
    return sorted(result)