def palindromes_of_specific_lengths(text):
    if len(text) < 96:
        return set()
    substring = text[75:96]
    substring = ''.join(filter(str.isalpha, substring)).lower()
    seen_palindromes = set()
    for length in range(7, 10):
        for start in range(len(substring) - length + 1):
            part = substring[start:start + length]
            if part == part[::-1]:
                seen_palindromes.add(part)
    return seen_palindromes