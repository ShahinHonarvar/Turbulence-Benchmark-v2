def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    for length in (3, 4):
        for idx in range(len(s) - length + 1):
            substr = s[idx:idx + length].lower()
            if substr == substr[::-1] and substr.isalpha():
                palindrome_set.add(substr)
    return palindrome_set