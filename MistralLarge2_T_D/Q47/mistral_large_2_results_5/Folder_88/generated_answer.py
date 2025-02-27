def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    result = set()
    relevant_substring = s[11:88].lower()
    for length in range(4, 6):
        for i in range(len(relevant_substring) - length + 1):
            substring = relevant_substring[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring)
    return result