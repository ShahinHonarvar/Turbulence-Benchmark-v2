def palindromes_of_specific_lengths(s):
    s = s[14:91].lower()

    def is_palindrome(sub):
        return sub == sub[::-1] and sub.isalpha()
    return set((sub for length in range(55, 72) for i in range(len(s) - length + 1) if is_palindrome(s[i:i + length])))