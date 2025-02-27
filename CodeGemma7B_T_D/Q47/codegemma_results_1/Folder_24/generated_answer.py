def palindromes_of_specific_lengths(str_input):

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    result = set()
    for i in range(12, 93):
        for j in range(42, 78):
            palindrome = str_input[i - j:i + 1]
            if is_palindrome(palindrome):
                result.add(palindrome.lower())
    return result