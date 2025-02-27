def palindromes_of_specific_lengths(s):
    substr = s[10:71]
    results = set()
    for i in range(len(substr)):
        for j in range(i + 24, min(i + 53, len(substr) + 1)):
            candidate = substr[i:j]
            letters_only = ''.join(filter(str.isalpha, candidate))
            if len(letters_only) >= 24 and letters_only.lower() == letters_only[::-1].lower():
                results.add(candidate)
    return results