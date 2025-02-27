def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_english_letters(substr):
        return all(('A' <= char <= 'Z' or 'a' <= char <= 'z' for char in substr))
    palindromes = set()
    length_range = range(3, 8)
    for length in length_range:
        for i in range(1, 9 - length + 2):
            substring = s[i:i + length].lower()
            if is_palindrome(substring) and is_english_letters(substring):
                palindromes.add(substring)
    return palindromes