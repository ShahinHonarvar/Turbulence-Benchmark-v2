def palindromes_of_specific_lengths(s):

    def is_palindrome(st):
        return st == st[::-1]
    s = s.lower()
    substr = s[15:96]
    letters_only = ''.join((ch for ch in substr if ch.isalpha()))
    palindromes_set = set()
    for length in range(20, 67):
        for start in range(len(letters_only) - length + 1):
            candidate = letters_only[start:start + length]
            if is_palindrome(candidate):
                palindromes_set.add(candidate)
    return palindromes_set