def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        substr = substr.lower()
        return substr == substr[::-1]
    s = s[100:201]
    palindromes_set = set()
    n = len(s)
    for i in range(n):
        for length in range(5, 11):
            if i + length <= n:
                candidate = s[i:i + length]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes_set.add(candidate.lower())
    return palindromes_set