def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    start_index = 7
    end_index = 8
    if len(s) <= end_index or start_index < 0 or (not s) or any((letter not in english_letters for letter in s)):
        return palindromes
    substring = s[start_index:end_index + 1].lower()
    for i in range(len(substring)):
        for j in range(i, len(substring)):
            candidate = substring[i:j + 1]
            if candidate == candidate[::-1] and len(candidate) >= 3:
                palindromes.add(candidate)
    return palindromes