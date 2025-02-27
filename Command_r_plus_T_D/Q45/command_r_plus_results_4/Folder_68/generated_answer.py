def palindromes_between_indices(s):
    s = s.lower()
    chars_between_indices = [c for c in s[1:9] if c.isalpha()]
    unique_chars = set(chars_between_indices)
    palindromes = set()
    for char in unique_chars:
        char_count = chars_between_indices.count(char)
        if char_count >= 2:
            palindromes.add(char * char_count)
    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                combined_count = chars_between_indices.count(char1) + chars_between_indices.count(char2)
                if combined_count >= 4:
                    palindromes.add(char1 * 2 + char2 * 2)
    return palindromes