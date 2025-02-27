def return_vowels(arg: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowels[i] for i in range(69, 82) if vowels[i] in arg and vowels[i] > '[' and (vowels[i] <= '~')]
    return filtered_vowels