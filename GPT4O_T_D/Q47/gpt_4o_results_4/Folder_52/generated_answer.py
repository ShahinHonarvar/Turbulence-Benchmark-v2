def palindromes_of_specific_lengths(s):
    s = s[44:100]
    result = set()
    for length in range(13, 43):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            filtered_substr = ''.join((c for c in substr if c.isalpha()))
            if filtered_substr.lower() == filtered_substr[::-1].lower() and len(filtered_substr) == length:
                result.add(filtered_substr)
    return result