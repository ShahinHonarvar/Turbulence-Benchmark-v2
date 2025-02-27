def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower)):
        for j in range(i + 42, len(s_lower) + 1):
            sub_s = s_lower[i:j]
            if all((c.isalpha() for c in sub_s)) and is_palindrome(sub_s):
                palindromes.add(sub_s)
    return palindromes