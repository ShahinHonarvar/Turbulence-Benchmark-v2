def palindromes_of_specific_lengths(s):
    s = s[35:88].lower()
    return {word for word in s.split() if word.isalpha() and 24 <= len(word) <= 33 and (word == word[::-1])}