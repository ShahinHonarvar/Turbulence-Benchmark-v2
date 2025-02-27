def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:8].lower()))
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(5, len(letters) + 1):
        if length > len(letters):
            break
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes