def palindromes_of_specific_lengths(s):
    filtered_substring = ''.join((c.lower() for c in s[26:88] if c.isalpha()))
    result = set()
    for length in range(52, 57):
        for i in range(len(filtered_substring) - length + 1):
            sub = filtered_substring[i:i + length]
            if sub == sub[::-1]:
                result.add(sub)
    return result