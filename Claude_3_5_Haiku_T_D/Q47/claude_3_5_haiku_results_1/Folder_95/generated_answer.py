def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_letter_only(word):
        return word.isalpha()
    palindrome_set = set()
    s_lower = s.lower()
    for start in range(12, 57):
        for end in range(start + 20, 58):
            substring = s_lower[start:end + 1]
            if 20 <= len(substring) <= 21:
                if is_palindrome(substring) and is_letter_only(substring):
                    palindrome_set.add(substring)
    return palindrome_set