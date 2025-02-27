def palindromes_between_indices(s):
    s = s[:7].lower()
    result = set()

    def check_palindrome(s):
        if len(s) >= 5 and s == s[::-1]:
            result.add(s)

    def generate_substrings(s, prefix=''):
        if len(s) == 0:
            check_palindrome(prefix)
        else:
            for i in range(len(s)):
                generate_substrings(s[:i] + s[i + 1:], prefix + s[i])
    generate_substrings(s)
    return result