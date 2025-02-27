def palindromes_between_indices(s: str) -> set[str]:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    s_lower = s[3:10].lower()
    s_lower_english_only = ''.join((char for char in s_lower if char in english_letters))
    for i in range(len(s_lower_english_only) - 4):
        for j in range(i + 1, len(s_lower_english_only) - i):
            substring = s_lower_english_only[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes