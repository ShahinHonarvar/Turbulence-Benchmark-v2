def palindromes_between_indices(s):
    relevant_chars = [c for c in s[5:7] if c.isalpha()]
    relevant_chars_lower = [c.lower() for c in relevant_chars]
    palindromes = set()
    for i in range(len(relevant_chars_lower)):
        for j in range(i, len(relevant_chars_lower)):
            for k in range(j, len(relevant_chars_lower)):
                candidate = relevant_chars_lower[i] + relevant_chars_lower[j] + relevant_chars_lower[k]
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes