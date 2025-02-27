def palindromes_of_specific_lengths(string):
    palindrome_set = set()
    substring = string[15:96]
    for length in range(20, 67):
        for start in range(len(substring) - length + 1):
            word = substring[start:start + length].lower()
            if word == word[::-1] and word.isalpha():
                palindrome_set.add(word)
    return palindrome_set