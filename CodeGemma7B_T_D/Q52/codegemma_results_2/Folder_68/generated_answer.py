def palindrome_of_length_n(str):

    def is_palindrome(word):
        return word == word[::-1]

    def find_palindromes(str, start, end, size):
        palindromes = set()
        if end + size > len(str):
            return palindromes
        for i in range(end, end + size):
            if is_palindrome(str[start:i + 1]):
                palindromes.add(str[start:i + 1].lower())
        next_palindrome = find_palindromes(str, start - 1, end, size)
        palindromes.update(next_palindrome)
        next_palindrome = find_palindromes(str, start, end + 1, size)
        palindromes.update(next_palindrome)
        return palindromes
    if len(str) < 76:
        return set()
    return find_palindromes(str, len(str) - 76, len(str) - 75, 76)