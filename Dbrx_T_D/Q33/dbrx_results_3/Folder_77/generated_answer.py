def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    start_index = 837
    end_index = 975
    for i in range(start_index, end_index):
        if s[i] > 'N' and s[i] <= 'W' and (s[i] in vowels):
            result.append(s[i])
    return result