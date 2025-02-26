def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[12:93]

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    for i in range(len(substring)):
        for j in range(i + 17, min(i + 67, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha() and is_palindrome(potential_palindrome):
                result.add(potential_palindrome)
    return result