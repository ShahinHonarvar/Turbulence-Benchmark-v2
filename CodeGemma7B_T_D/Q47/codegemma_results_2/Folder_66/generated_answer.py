def palindromes_of_specific_lengths(str):

    def is_palindrome(word):
        return word == word[::-1]
    result = set()
    for i in range(32, 79 + 1):
        for j in range(35, 41 + 1):
            word = str[i:i + j].lower()
            if is_palindrome(word) and word.isalpha():
                result.add(word)
    return result