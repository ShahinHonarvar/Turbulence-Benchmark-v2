def palindromes_of_specific_lengths(text):

    def is_palindrome(text):
        text = text.lower()
        return text == text[::-1]
    result = set()
    for i in range(32, 72):
        for j in range(21, 33):
            palindrome = text[i - j:i + j + 1]
            if is_palindrome(palindrome) and palindrome.isalpha():
                result.add(palindrome)
    return result