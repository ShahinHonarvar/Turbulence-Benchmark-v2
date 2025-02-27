def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq.lower() == seq[::-1].lower()
    s = s[:31]
    possible_palindromes = set()
    for start in range(len(s)):
        for end in range(start + 20, min(start + 31, len(s) + 1)):
            substr = s[start:end]
            if substr.isalpha() and is_palindrome(substr):
                possible_palindromes.add(substr)
    return possible_palindromes