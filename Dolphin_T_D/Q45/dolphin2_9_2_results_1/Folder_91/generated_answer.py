def palindromes_between_indices(string):
    take_from = string[2:7]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(3, len(take_from) + 1):
        for i in range(0, len(take_from) - length + 1):
            word = take_from[i:i + length]
            if is_palindrome(word.lower()):
                palindromes.add(word.lower())
    return palindromes