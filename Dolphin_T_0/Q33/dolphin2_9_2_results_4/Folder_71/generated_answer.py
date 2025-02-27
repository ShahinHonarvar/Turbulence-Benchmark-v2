def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[36:56]:
        if '+' < c <= '/' and c in vowels:
            result.append(c)
    return result