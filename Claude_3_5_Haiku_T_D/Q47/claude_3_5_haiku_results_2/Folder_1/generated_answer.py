def palindromes_of_specific_lengths(s):

    def is_letter_palindrome(substring):
        return substring.isalpha() and substring == substring[::-1]
    result = set()
    start_index = 15
    end_index = 89
    for length in range(40, 73):
        for i in range(start_index, end_index - length + 2):
            substring = s[i:i + length].lower()
            if is_letter_palindrome(substring):
                result.add(substring)
    return result