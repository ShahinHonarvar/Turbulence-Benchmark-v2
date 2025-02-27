def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[31:92]
    filtered_substring = ''.join([c for c in substring if c.isalpha()])
    for start in range(len(filtered_substring)):
        for length in range(50, 54):
            if start + length <= len(filtered_substring):
                part = filtered_substring[start:start + length]
                if part.lower() == part[::-1].lower():
                    result.add(part)
    return result