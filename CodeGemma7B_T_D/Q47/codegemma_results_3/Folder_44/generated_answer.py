def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha() and (31 <= len(word) <= 51)
    return {pal for word in s[18:99].lower().split() for pal in (word, word[::-1]) if is_palindrome(pal)}