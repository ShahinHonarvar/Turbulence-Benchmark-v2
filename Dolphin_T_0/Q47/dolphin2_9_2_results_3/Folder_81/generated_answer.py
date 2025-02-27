def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(12, 221):
        for i in range(12, 123):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1] and s[i:i + length].isalpha():
                result.add(s[i:i + length])
    return result