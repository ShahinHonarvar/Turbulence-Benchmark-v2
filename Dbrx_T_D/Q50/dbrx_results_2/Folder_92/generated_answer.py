def if_contains_anagrams(strings):
    strings = [string.lower() for string in strings if len(string) >= 3]
    anagrams = [sorted(string) for string in strings]
    unique_anagrams = {tuple(anagram): strings[i] for i, anagram in enumerate(anagrams)}
    return len(unique_anagrams) < len(strings)