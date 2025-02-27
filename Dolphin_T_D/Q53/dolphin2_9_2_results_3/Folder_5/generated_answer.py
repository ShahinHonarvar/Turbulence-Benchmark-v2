def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    n = 46
    palindromes = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if all((c.isalpha() for c in sub)):
            palindromes.add(sub)
    return {p for p in palindromes if is_palindrome(p)}