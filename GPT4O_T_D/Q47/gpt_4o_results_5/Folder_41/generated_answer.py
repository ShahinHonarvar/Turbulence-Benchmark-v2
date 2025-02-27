def palindromes_of_specific_lengths(s):
    s = s[1:8]
    results = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s)):
            candidate = s[i:j + 1]
            letters_only = ''.join(filter(str.isalpha, candidate))
            if len(letters_only) in [3, 4] and letters_only.lower() == letters_only[::-1].lower():
                results.add(letters_only.lower())
    return results