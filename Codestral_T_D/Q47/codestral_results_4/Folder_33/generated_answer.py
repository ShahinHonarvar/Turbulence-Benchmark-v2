def palindromes_of_specific_lengths(s):
    s = s[130:296]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 103, min(start + 159, len(s))):
            sub = s[start:end]
            if sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes