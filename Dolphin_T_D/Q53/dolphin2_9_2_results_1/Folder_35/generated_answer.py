def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    set_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 26, len(s) + 1):
            sub_s = s[i:j]
            if is_palindrome(sub_s):
                set_palindromes.add(sub_s.lower())
    return set_palindromes