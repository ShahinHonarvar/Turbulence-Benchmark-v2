def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    english_letters = [c for c in s[2:7] if c.isalpha()]
    result = set()
    for i in range(4, len(english_letters) + 1):
        for j in range(len(english_letters) - i + 1):
            if english_letters[j:j + i] == english_letters[j:j + i][::-1]:
                result.add(''.join(english_letters[j:j + i]))
    return result