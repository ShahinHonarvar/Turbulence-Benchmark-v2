def palindromes_of_specific_lengths(s):
    if len(s) < 63:
        return set()
    substring = s[21:63].lower()
    palindrome_set = set()
    for length in range(22, 34):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindrome_set.add(candidate)
    return palindrome_set