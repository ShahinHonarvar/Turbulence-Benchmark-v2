def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    palindromes = set()
    s = s.lower()
    for length in range(13, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if len(substr.replace(' ', '').replace(',', '').replace('.', '')) == length:
                if all((c.isalpha() for c in substr.replace(' ', '').replace(',', '').replace('.', ''))):
                    if is_palindrome(substr.replace(' ', '').replace(',', '').replace('.', '')):
                        palindromes.add(substr.replace(' ', '').replace(',', '').replace('.', ''))
    return palindromes