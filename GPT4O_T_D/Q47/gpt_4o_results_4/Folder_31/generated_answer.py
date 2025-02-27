def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join([ch for ch in s.lower() if ch.isalpha()])
    substrings = [s[i:j] for i in range(min(len(s), 11), min(len(s), 84)) for j in range(i + 37, min(i + 61, len(s) + 1))]
    palindromes = {sub for sub in substrings if is_palindrome(sub)}
    return palindromes