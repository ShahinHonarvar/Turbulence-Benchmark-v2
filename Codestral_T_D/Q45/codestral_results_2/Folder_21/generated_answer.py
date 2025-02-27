def palindromes_between_indices(string):

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palindromes(s, left, right):
        if left > right:
            if len(s) >= 7 and is_palindrome(s):
                palindromes.add(s.lower())
            return
        for i in range(left, right + 1):
            s[left], s[i] = (s[i], s[left])
            generate_palindromes(s, left + 1, right)
            s[left], s[i] = (s[i], s[left])
    palindromes = set()
    substring = list(string[1:9])
    generate_palindromes(substring, 0, len(substring) - 1)
    return palindromes