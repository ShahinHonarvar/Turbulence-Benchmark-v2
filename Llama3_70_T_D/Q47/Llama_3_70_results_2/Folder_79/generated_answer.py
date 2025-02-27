def palindromes_of_specific_lengths(s):
    s = s[1:9].lower()

    def is_palindrome(s):
        return s == s[::-1]
    return set((s[i:j] for i in range(len(s)) for j in range(i + 3, min(i + 5, len(s) + 1)) if s[i:j].isalpha() and is_palindrome(s[i:j])))