def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[12:39] if ';' < c <= '|' and c in vowels]
    if not result:
        return []
    return result