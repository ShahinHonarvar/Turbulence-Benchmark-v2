def palindromes_of_specific_lengths(text):

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    result = set()
    start_idx = 0
    end_idx = 4
    for i in range(start_idx, end_idx + 1):
        for j in range(i + 1, end_idx + 1):
            word = text[i:j + 1]
            if 3 <= len(word) <= 4 and is_palindrome(word):
                result.add(word)
    return result