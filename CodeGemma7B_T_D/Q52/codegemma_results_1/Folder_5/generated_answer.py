def palindrome_of_length_n(string):

    def is_palindrome(word):
        return word == word[::-1]
    lowercase_str = string.lower()
    palindromes = set()
    for i in range(len(lowercase_str)):
        for j in range(i + 1, len(lowercase_str)):
            substring = lowercase_str[i:j + 1]
            if is_palindrome(substring) and len(substring) == 17:
                palindromes.add(substring)
    return palindromes