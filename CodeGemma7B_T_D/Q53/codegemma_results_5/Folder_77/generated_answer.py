def palindrome_of_length_at_least_n(text):
    n = 149
    palindrome_set = set()
    text = text.lower().replace(' ', '')

    def is_palindrome(string):
        return string == string[::-1]
    for i in range(len(text) - n + 1):
        for j in range(i + n, len(text) + 1):
            substring = text[i:j]
            if is_palindrome(substring) and len(substring) >= n:
                palindrome_set.add(substring)
    return palindrome_set