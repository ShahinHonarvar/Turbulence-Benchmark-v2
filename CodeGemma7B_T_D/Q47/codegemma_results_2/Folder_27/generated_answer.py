def palindromes_of_specific_lengths(string):
    lower_string = string.lower()
    return {word for word in lower_string[13:99 + 1].split() if 26 <= len(word) <= 29 and word == word[::-1] and word.isalpha()}