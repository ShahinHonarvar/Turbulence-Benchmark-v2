def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    result = set()
    substring = s[12:57]
    for i in range(len(substring) - 19):
        for length in range(20, 22):
            if i + length <= len(substring):
                potential_palindrome = ''.join([char for char in substring[i:i + length] if char.isalpha()])
                if is_palindrome(potential_palindrome) and len(potential_palindrome) == length:
                    result.add(potential_palindrome)
    return result