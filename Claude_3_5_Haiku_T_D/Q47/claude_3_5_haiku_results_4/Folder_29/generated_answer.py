def palindromes_of_specific_lengths(text):
    palindrome_set = set()
    substring = text[15:95].lower()
    for length in range(18, 74):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) == length and candidate == candidate[::-1] and candidate.isalpha():
                palindrome_set.add(candidate)
    return palindrome_set