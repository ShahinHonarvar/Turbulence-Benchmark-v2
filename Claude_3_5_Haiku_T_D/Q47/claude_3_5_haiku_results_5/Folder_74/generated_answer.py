def palindromes_of_specific_lengths(s):
    palindromes = set()
    sub_s = s[30:85]
    for start in range(len(sub_s)):
        for end in range(start + 11, min(start + 21, len(sub_s))):
            candidate = sub_s[start:end + 1]
            if candidate.lower() == candidate.lower()[::-1] and candidate.replace(' ', '').isalpha():
                palindromes.add(candidate)
    return palindromes