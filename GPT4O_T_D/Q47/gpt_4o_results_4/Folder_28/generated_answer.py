def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    filtered_text = ''.join((c for c in text[32:72] if c.isalpha())).lower()
    palindromes = set()
    for length in range(21, 33):
        for i in range(len(filtered_text) - length + 1):
            substring = filtered_text[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes