def palindromes_of_specific_lengths(s):
    s = s[:21].lower()

    def is_palindrome(sub):
        return sub == sub[::-1] and sub.isalpha()
    return set((sub for length in range(5, 81) for i in range(21 - length + 1) if is_palindrome(s[i:i + length])))