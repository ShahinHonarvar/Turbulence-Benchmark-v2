def return_vowels(s: str) -> list:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(770, 852):
        if i < len(s) and s[i] > 'B' and (s[i] <= 'i') and (s[i] in vowels):
            result.append(s[i])
    return result