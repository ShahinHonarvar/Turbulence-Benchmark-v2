def palindromes_of_specific_lengths(s):
    substring = s[28:95]
    result = set()

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    for i in range(len(substring)):
        for j in range(i + 38, min(i + 50, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha() and is_palindrome(potential_palindrome):
                result.add(potential_palindrome)
    return result