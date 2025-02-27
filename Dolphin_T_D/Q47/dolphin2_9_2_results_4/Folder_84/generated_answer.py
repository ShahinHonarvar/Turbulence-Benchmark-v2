def palindromes_of_specific_lengths(s):
    s = s[22:78]
    palindromes_set = set()
    for length in range(13, 41):
        for i in range(len(s)):
            sub = s[i:i + length]
            if sub == sub[::-1] and all((c.isalpha() for c in sub)):
                palindromes_set.add(sub.lower())
    return palindromes_set