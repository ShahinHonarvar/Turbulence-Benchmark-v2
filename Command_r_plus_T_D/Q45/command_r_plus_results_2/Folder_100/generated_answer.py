def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    chars_between_indices = set((s[i] for i in range(6)))
    chars_between_indices.discard(' ')
    chars_between_indices.discard(',')
    chars_between_indices.discard('.')
    chars_between_indices.discard('?')
    chars_between_indices.discard('!')
    palindromes = set()
    for char in chars_between_indices:
        palindrome = char + char[::-1]
        if len(palindrome) >= 6:
            palindromes.add(palindrome)
    return palindromes