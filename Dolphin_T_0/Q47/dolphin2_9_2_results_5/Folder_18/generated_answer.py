def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        s = s.lower()
        return all((s[i] == s[~i] for i in range(len(s) // 2)))
    return {s[i:j] for i in range(11, 84) for j in range(i + 13, 84) if is_palindrome(s[i:j]) and s[i:j].isalpha() and (13 <= j - i <= 66)}