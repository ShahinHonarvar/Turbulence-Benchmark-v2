def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 98, len(s)):
            subs = s[i:j + 1]
            if is_palindrome(subs) and subs.isalpha():
                palindromes.add(subs)
    return palindromes