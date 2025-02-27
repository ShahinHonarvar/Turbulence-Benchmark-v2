def palindromes_of_specific_lengths(s):
    s = s[62:89]
    s_letters_only = ''.join(filter(str.isalpha, s))
    s_lower = s_letters_only.lower()
    results = set()
    for length in range(18, 22):
        for i in range(len(s_lower) - length + 1):
            substring = s_lower[i:i + length]
            if substring == substring[::-1]:
                results.add(s_letters_only[i:i + length])
    return results