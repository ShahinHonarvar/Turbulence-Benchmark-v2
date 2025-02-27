def palindrome_of_length_at_least_n(txt):
    min_palindrome_length = 70
    result = set()

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    for i in range(len(txt) - min_palindrome_length + 1):
        for j in range(i + min_palindrome_length - 1, len(txt)):
            substring = txt[i:j + 1]
            if is_palindrome(substring):
                result.add(substring)
    return result