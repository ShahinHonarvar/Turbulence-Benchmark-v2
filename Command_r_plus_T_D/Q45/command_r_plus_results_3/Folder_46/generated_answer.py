def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s_range = s[4:10].lower()
    s_range_letters = set(s_range)
    english_letters_in_range = english_letters.intersection(s_range_letters)
    s_range_letters_in_range = ''.join(s_range_letters)
    palindromes = set()
    for i in range(len(s_range_letters_in_range) - 5):
        for j in range(i + 6, len(s_range_letters_in_range) + 1):
            substring = s_range_letters_in_range[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes