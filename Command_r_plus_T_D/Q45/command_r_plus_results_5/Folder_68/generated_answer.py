def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    english_letters = [c for c in s[1:9] if c.isalpha()]
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 4, len(english_letters) + 1):
            substring = english_letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes